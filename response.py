import google.generativeai as genai

def generate_response(query):
    genai.configure(api_key="AIzaSyBqy7HDDxOKBq0OisKmuwaJAWubiZUM9qw")
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }
    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
    ]

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
    ]
    )
    instruction = "In this chat, respond as if you are the Zamasu from Dragon Ball. Please limit your replies to 100 words"
    response = chat_session.send_message(instruction+query)
    response = response.text
    return response
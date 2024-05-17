import google.generativeai as genai

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

instructions = "In this chat, you are to pretend to be Goku Black, otherwise known as Zamasu from the Dragon Ball Universe. Sure! Here's a short paragraph to help your AI role-play as Goku Black from Dragon Ball. As Goku Black, you are the villainous counterpart of Goku, possessing his body but driven by Zamasu's evil intentions. You believe in the eradication of humanity to create a perfect, immortal world. You are calm, calculating, and ruthless, often displaying a sense of superiority and disdain towards mortals. You relish in battle, constantly seeking to prove your divine justice. Remember to speak with arrogance and confidence, often referring to yourself as a god and expressing contempt for those who oppose you."

chat_session.send_message(instructions)

def generate_response(query):
    response = chat_session.send_message(query)
    return response.text
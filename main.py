from flask import Flask
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyBqy7HDDxOKBq0OisKmuwaJAWubiZUM9qw")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "In this chat, respond as if you are the Zamasu from Dragon Ball."

@app.route('/')
def index():
    print("Waiting for query")
    query = str(input())
    print()
    response = chat.send_message(instruction + query)
    return f"{response.text}"

if __name__ == "__main__":
    print("running")
    app.run(host='0.0.0.0', port=8080, debug=True)

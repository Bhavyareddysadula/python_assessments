from flask import Flask, render_template, request, session
from langchain_mistralai.chat_models import ChatMistralAI
from langchain.schema import HumanMessage, AIMessage
import os

app = Flask(__name__)
app.secret_key = 'mykey123'

os.environ["MISTRAL_API_KEY"] = "PHhuPwA28efvLjGbbXBdfDXx0XwjKjNP" # setting up the mistral ai key to os environment

llm = ChatMistralAI(model="open-mistral-nemo") # chat model is mistal ai

def chatbot(history):
    messages = []
    for msg in history:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))
    return messages

@app.route('/', methods=['GET', 'POST'])
def chat():
    if "history" not in session:
        session["history"] = []
    result = ""
    if request.method == 'POST':
        user_input = request.form['query']
        session["history"].append({"role": "user", "content": user_input})
        chat_history = chatbot(session["history"])    # for generating the response
        response = llm(chat_history)
        bot_reply = response.content
        session["history"].append({"role": "assistant", "content": bot_reply})
        session.modified = True
        result = bot_reply
    return render_template("chat.html", history=session["history"], result=result)

@app.route('/reset')
def reset():
    session.clear()
    return "Chat history cleared!"

if __name__ == "__main__":
    app.run(debug=True)

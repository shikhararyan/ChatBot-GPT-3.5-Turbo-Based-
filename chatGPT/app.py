from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'enter your openai API key'

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_with_gpt():
    content = request.json['message']
    if content:
        messages.append(
            {"role": "user", "content": content}
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})
    return jsonify({"error": "Empty message"}), 400

if __name__ == '__main__':
    app.run(debug=True)

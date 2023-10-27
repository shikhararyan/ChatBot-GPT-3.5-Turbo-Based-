from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = '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'

messages = []

@app.route('/')
def index():
    return render_template('index1.html')

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

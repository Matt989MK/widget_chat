from flask import Flask, request, jsonify, render_template
from db import get_info, update_info
from chatbot import generate_response

app = Flask(__name__)

@app.route('/')
def home():
    info = get_info()
    return render_template('home.html', info=info)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Extract message from webhook data
    message = data['text']

    # Generate response using chatbot logic
    response = generate_response(message)

    # Update database with any new information gathered from the conversation
    update_info(message, response)

    # Return response to webhook
    return jsonify({'text': response})
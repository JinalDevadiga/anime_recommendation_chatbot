from flask import Flask, render_template, request, jsonify, Response
import openai
import json

API_KEY = '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'

app = Flask(__name__)

messages = [
    {
        'role' : 'system',
        'content' : 'You are an assistant that has the knowledge of different genres of anime with their ratings. You can suggest anime with their ratings on the basis of the genre provided.'
    },
    {
        'role' : 'user',
        'content' : ''
    }
]

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/animeRecommeder', methods=['POST'])
def anime_recommendation():
    try:
        openai.api_key = API_KEY
        data = request.get_json()
        question = data.get('parameter')
        global messages
        messages[1]['content'] = question
        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = messages,
            # max_tokens =50,
        )
        print(response.choices[0]['message']['content'])
        return jsonify({'bot_response': response.choices[0]['message']['content']})
    except Exception as e:
        print('Error occurred: ',str(e))
        return jsonify(jsonify({'error': 'An error occurred'}))
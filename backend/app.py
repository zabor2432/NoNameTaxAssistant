from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import openai

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')
load_dotenv()

@app.route("/chat/completions", methods=['POST'])
def connect():
    data = request.json
    prompt = data.get('prompt', '')
    model = data.get('model','')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        response = openai.Completion.create(
            model=model,  
            prompt=prompt,
            max_tokens=100
        )

        return response
        
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
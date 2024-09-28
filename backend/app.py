from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI
import json
import requests
import time
from openai import AzureOpenAI


app = Flask(__name__)

load_dotenv()
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
  api_key= os.getenv("AZURE_OPENAI_API_KEY"),
  api_version="2024-05-01-preview"
)


@app.route("/chat/completions", methods=['POST'])
def connect():
    data = request.json
    model = data.get('model','')
    messages = data.get('messages','')


    try:
        response = client.chat.completions.create(
            model=model,  
            messages=messages
        )

        return response


    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)

import json
import os

import json
import google.generativeai as genai


def load_ai():
    
    path = 'params\keys.json'

    with open(path, 'r') as file:
    # Load the JSON content from the file
        data = json.load(file)


    genai.configure(api_key=data['api-key'])

    # Set up the model
    generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
                                }

    
    model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              #safety_settings=safety_settings
                              )
    convo = model.start_chat(history=[])

    
    return convo




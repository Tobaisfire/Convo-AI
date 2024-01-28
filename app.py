
from flask import Flask, request, jsonify,render_template,redirect,session
from time import sleep
from LLM import *
import google.generativeai as genai
import os



app = Flask(__name__)

app.secret_key = 'MY-Convo'







@app.route('/')

def home():
    
    
        
    
    return render_template('chat.html')



@app.route('/send_message', methods=['POST'])
def get_response():
    # user = session['user']
    
    user_message = request.form.get('user_message')
    

 
    bot_reply = generate_reply(user_message,ai_model)

    response = {
        'bot_reply': bot_reply
    }
    
    return jsonify(response)





def generate_reply(message,model):



    query = message

    response= convo(model,str(query))

    AI = response[0]
  
    return AI


app.run()
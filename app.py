
from flask import Flask, request, jsonify,render_template,redirect,session
from time import sleep
from LLM import *
import google.generativeai as genai

app = Flask(__name__)

app.secret_key = 'MY-Convo'



ai_model = load_ai()
def convo(ai_model,query):


 
 
    ai_model.send_message(query)
    AI_MSG = ai_model.last.text
    # print(AI_MSG)
    chat_history = ai_model.history
    if len(ai_model.history) >= 50:
        ai_model.history.clear()
    
    return AI_MSG,chat_history



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


app.run(debug=True)
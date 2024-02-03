
from flask import Flask, request, jsonify,render_template,session
from time import sleep
from LLM import *
import google.generativeai as genai

app = Flask(__name__)

app.secret_key = 'MY-Convo'





ai_model = load_ai()






@app.route('/',methods=['GET','POST'])

def home():

    if request.method == 'POST':
  
        if request.form.get('name') != None and  request.form.get('name') != "" :
            name = request.form.get('name')
            session['username'] = name
            print(session['username'] )
            return render_template('chat.html',user = name)
        
        

    return render_template('id_fecther.html')



@app.route('/send_message', methods=['POST'])
def get_response():
    user = session['username']
 
    
    user_message = request.form.get('user_message')
    

 
    bot_reply = generate_reply(user_message,ai_model,username=user)

    response = {
        'bot_reply': bot_reply
    }



    
    return jsonify(response)





def generate_reply(message,model,username):



    query = message

    response = convo(model,str(query))

    AI = response[0]

    

  
    return AI

app.run(debug=True)




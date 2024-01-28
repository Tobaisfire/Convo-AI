
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




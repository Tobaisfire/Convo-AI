
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai

from langchain.prompts import PromptTemplate

def load_ai():
    # llm = GoogleGenerativeAI(model="gemini-pro", google_api_key='AIzaSyBdEqD6KR5oRrzNXb2qjvcOjnpjzU9uR0w')


    # template = """our are a smart and helpful assitant name tobi and help user by giving appropriate response of user Queries.
    #             Note you are an assitant created by keval Saud .

       
          
    #             Queries: {Queries}"""
    
    # prompt = PromptTemplate.from_template(template)

    # convo = prompt | llm

    genai.configure(api_key='api-key')

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




def convo(ai_model,query):


    # response = ai_model.invoke({"Queries": query})
 
    ai_model.send_message(query)
    response = ai_model.last.text
    # print(AI_MSG)
    history = ai_model.history
    if len(ai_model.history) >= 50:
        ai_model.history.clear()
    history= [{'user': query,'AI': response}]
    return response,history



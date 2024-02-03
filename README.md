# Convo-AI
Chat AI Using Gemini-Pro by Google DeepMind !

# Convo-AI
Using AI Gemini-Pro !

# Gemini API Quickstart

Welcome to the Gemini API Quickstart! This project leverages the Gemini API to generate content using Google Colab. You can run this notebook directly in your browser, or if you prefer, set it up locally.

## Prerequisites

Before you begin, make sure you meet the following requirements:

- Python 3.9+
- Jupyter installed to run the notebook.

Alternatively, you can run this quickstart in Google Colab without additional environment configuration.

## Setup

### Install the Python SDK

The Gemini API Python SDK is contained in the `google-generativeai` package. Install it using pip:

```bash
pip install -q -U google-generativeai
```
### Install requiremesnt.txt

```bash
pip install  -r requirements.txt
```


## Setup Your API Key

Before using the Gemini API, obtain an API key. If you don't have one, create a key with one click in Google AI Studio. In Colab, add the key to the secrets manager under the "🔑" in the left panel and name it GOOGLE_API_KEY.

Once you have the API key, pass it to the SDK. You can do this in two ways:

Put the key in the GOOGLE_API_KEY environment variable.
Pass the key to genai.configure(api_key=...).

```
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
```

### Run Flask app 

```bash
python run app.py

Running on http://127.0.0.1:5000
```
Go to Link and Talk with AI

##CHAT-AI
![image](https://github.com/Tobaisfire/Convo-AI/assets/67000746/588981ab-8dcf-4af6-bf1d-67ab0dafbac4)


### Models Available :
Note: Detailed information about the available models, including capabilities and rate limits, can be found in the Gemini models documentation. Rate limits for Gemini-Pro models are set at 60 requests per minute (RPM).

## Gemini-Pro (TEXT TO TEXT MODEL) : 

## Generate Text from Text Inputs
For text-only prompts, use the gemini-pro model:

```
model = genai.GenerativeModel('gemini-pro')
%%time
response = model.generate_content("What is the meaning of life?")
to_markdown(response.text)
```

### Feel free to explore and experiment with the Gemini API using this quickstart guide! If you have any questions or need further assistance, refer to the official Gemini API documentation : https://ai.google.dev/docs.






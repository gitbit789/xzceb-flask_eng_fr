import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['XsiMab4QJXq0YVJnvd1lZNDwuiEUlDEqgdgjyJYBucj5']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/b834e099-f8e9-487f-84be-88c7cbcbf7e4']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version = '2018-05-01',
authenticator = authenticator)

language_translator.set_service_url(url)


def english_to_french(english_text):
    
    #Translates English to French
    
    translation = language_translator.translate(\
        text = english_text, model_id= 'en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text1):
    
    #Translates French to English
    
    translation = language_translator.translate(\
        text = french_text1, model_id= 'fr-en').get_result()
    english_text1 = translation['translations'][0]['translation']
    return english_text1





    
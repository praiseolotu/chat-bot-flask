import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

'''
Authenticating my api key
'''
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def engToFrench(request):
    """
    Translate English to French
    """
    if request is None:
        return None
    response = language_translator.translate(text=request,model_id="en-fr").get_result()
    translation = response['translations'][0]['translation']
    return translation



def frenchToEng(request):
    """
    Translate French to English
    """
    if request is None:
        return None
    response = language_translator.translate(text=request,model_id="fr-en").get_result()
    translation = response['translations'][0]['translation']
    return translation

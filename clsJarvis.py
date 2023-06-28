#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 27-Jun-2023                     ####
#### Modified On 28-Jun-2023                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python class that will invoke the           ####
#### Flask framework to expose the OpenAI        ####
#### API with more control & encapsulate the     ####
#### server IPs with proxy layers.               ####
####                                             ####
#####################################################

import openai
from flask import request, jsonify

from clsConfigClient import clsConfigClient as cf
import os

import clsTemplate as ct
###############################################
###           Global Section                ###
###############################################
open_ai_Key = cf.conf['OPEN_AI_KEY']
openai.api_key = open_ai_Key

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

###############################################
###    End of Global Section                ###
###############################################

class clsJarvis:
    def __init__(self):
        self.model_name = cf.conf['MODEL_NAME']
        self.max_token = cf.conf['MAX_TOKEN']
        self.temp_val = cf.conf['TEMP_VAL']

    def extractContentInText(self, query):
        try:
            model_name = self.model_name
            max_token = self.max_token
            temp_val = self.temp_val

            template = ct.templateVal_1

            response = openai.ChatCompletion.create(model=model_name, temperature=temp_val, messages=[{"role": "system", "content": template},{"role": "user", "content": query}])
            inputJson = {"text": response['choices'][0]['message']['content']}

            return jsonify(inputJson)
        except Exception as e:
            discussedTopic = []
            x = str(e)
            print('Error: ', x)
            template = ct.templateVal_2

            inputJson = {"text": template}

            return jsonify(inputJson)

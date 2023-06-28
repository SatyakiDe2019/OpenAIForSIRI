#########################################################
#### Written By: SATYAKI DE                          ####
#### Written On: 27-Jun-2023                         ####
#### Modified On 28-Jun-2023                         ####
####                                                 ####
#### Objective: This is the main calling             ####
#### python script that will invoke the              ####
#### shortcut application created inside MAC         ####
#### enviornment including MacBook, IPad or IPhone.  ####
####                                                 ####
#########################################################

import clsL as cl
from clsConfigClient import clsConfigClient as cf
import clsJarvis as jv
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)


# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

######################################
### Get your global values        ####
######################################
debug_ind = 'Y'

# Initiating Logging Instances
clog = cl.clsL()

cJarvis = jv.clsJarvis()

######################################
####         Global Flag      ########
######################################
@app.route('/openai', methods=['POST'])
def openai_call():
    try:
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('*'*120)
        print('Start Time: ' + str(var))
        print('*'*120)

        data = request.get_json()
        print('Data::')
        print(data)
        prompt = data.get('prompt', '')

        print('Prompt::')
        print(prompt)

        res = cJarvis.extractContentInText(str(prompt))

        return res

        print('*'*120)
        var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('End Time: ' + str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

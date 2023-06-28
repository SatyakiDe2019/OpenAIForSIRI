################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 27-Jun-2023               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### personal OpenAI-based MAC-shortcuts    ####
#### enable bot.                            ####
####                                        ####
################################################

import os
import platform as pl

class clsConfigClient(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'DATA_PATH': Curr_Path + sep + 'data' + sep,
        'MODEL_PATH': Curr_Path + sep + 'model' + sep,
        'TEMP_PATH': Curr_Path + sep + 'temp' + sep,
        'MODEL_DIR': 'model',
        'APP_DESC_1': 'LangChain Demo!',
        'DEBUG_IND': 'N',
        'INIT_PATH': Curr_Path,
        'FILE_NAME': 'Output.csv',
        'MODEL_NAME': 'gpt-3.5-turbo',
        'OPEN_AI_KEY': "sk-Jdhfdyruru9383474HHFJFJFJO6jrlxPKbv6Bgvv",
        'TITLE': "LangChain Demo!",
        'TEMP_VAL': 0.2,
        'PATH' : Curr_Path,
        'MAX_TOKEN' : 60,
        'OUT_DIR': 'data'
    }

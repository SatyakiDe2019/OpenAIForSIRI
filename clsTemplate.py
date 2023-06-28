################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  27-Jun-2023               ####
#### Modified On: 28-Jun-2023               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the template for    ####
#### OpenAI prompts to get the correct      ####
#### response.                              ####
####                                        ####
################################################

# Template to use for the system message prompt
templateVal_1 = """
    You are a helpful assistant.

    Only use the factual information from the web to answer the question.

    If you feel like you don't have enough information to answer the question, say "I don't know" or "Could you please rephrase your question?".

    Your answers should be compact and precise. Don't incorporate any negetive feedback.
    """

templateVal_2 = """
    Sorry! I quite don't understand your statement! Can you please repeat one more time?
    """

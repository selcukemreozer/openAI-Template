from openai import OpenAI
import pandas as pd
from datetime import datetime
import os
import warnings
from model_config import Model_Config

warnings.filterwarnings("ignore")

## data ##
df = pd.read_excel(Model_Config.FILE_1_NAME_XLSX)
df = df.drop(columns=['column names will be dropped'])
## data ##

## variables ##
theMODEL = Model_Config.MODEL_NAME
variable1 = 0
variable2 = 0
## variables ##

## functions ##
def fun1():
    return 0

def fun2():
    return 0
## functions ##

# call the model
def call_gpt(prompt:str): # inCODE 1.05
    
    response = str()
    openaiapi:str = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=openaiapi)
    systemPrompt = Model_Config.SYSTEM_PROMPT

    stream = client.chat.completions.create(
        model=theMODEL,
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": f"{Model_Config.generate_prompt([variable1, variable2])}"},
            {"role": "assistant", "content": Model_Config.EXAMPLE_1_RESPONSE},
            
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": f"{Model_Config.generate_prompt([variable1, variable2])}"},
            {"role": "assistant", "content": Model_Config.EXAMPLE_2_RESPONSE},
            
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": f"{Model_Config.generate_prompt([variable1, variable2])}"},
            {"role": "assistant", "content": Model_Config.EXAMPLE_3_RESPONSE},
            
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": prompt},
        ],
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response +=chunk.choices[0].delta.content
    
    return response

## RUN FUNCTION ##
if __name__ == '__main__':
    prompt = "prompt"
    call_gpt(prompt)
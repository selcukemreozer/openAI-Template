from openai import OpenAI
import pandas as pd
from datetime import datetime
import os
import warnings
from model_config import Model_Config

warnings.filterwarnings("ignore")

df = pd.read_excel(Model_Config.FILE_1_NAME_XLSX)
df = df.drop(columns=['columns will be dropped'])
## variables ##
theMODEL = Model_Config.MODEL_NAME
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
    
    demo1, qa1 = parameters(0) # demo1 > demographic, qa1 > question and answers
    demo2, qa2 = parameters(1)
    demo3, qa3 = parameters(2)
    stream = client.chat.completions.create(
        model=theMODEL,
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": f"{Model_Config.generate_prompt(demo1, qa1)}"},
            {"role": "assistant", "content": Model_Config.EXAMPLE_1_RESPONSE},
            
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": f"{Model_Config.generate_prompt(demo2, qa2)}"},
            {"role": "assistant", "content": Model_Config.EXAMPLE_2_RESPONSE},
            
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": f"{Model_Config.generate_prompt(demo3, qa3)}"},
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
df['accumulator_new'] = ''
for index in range(df.shape[0]):
    demo, qa = parameters(index)
    response = call_gpt(Model_Config.generate_prompt(parameter_list=demo, question=qa)) # inCODE 1.08
    df['accumulator_new'][index] = response
    print(index,response,'\n')
    df.to_excel(f'72seg_10q_accumulator_fixed.xlsx', index=False)
"""
Long description of the file wıth technical syntax and details:
<class Model_Config> is a class that contains the configuration of the model.

The class contains the following attributes:
    - FILE_1_NAME_XLSX: The name of the file that contains the data in the xlsx format.
    - MODEL_NAME: The name of the model that will be used to fix the options.
    - SYSTEM_PROMPT: The prompt that will be used to generate the questions for the model.
    - EXAMPLES: The examples that will be used to test the model.

<generate_prompt> is a method that generates the prompt for the model.
    details:
        - parameter_list: The list of parameters that will be used in the prompt.
        - questionNumber: The number of the question that will be generated.
        - prompt_text: The generated prompt for the model. It is a dynamic text that contains the parameters 
        - returns: The generated prompt for the model.
"""
import pandas as pd
class Model_Config:
    FILE_1_NAME_XLSX = 'test_data.csv'
    MODEL_NAME = 'gpt-4o-mini'
    SYSTEM_PROMPT = """
        """
        
    EXAMPLE_1_RESPONSE = ""
    EXAMPLE_2_RESPONSE = ""
    EXAMPLE_3_RESPONSE = ""
    
        
    def __init__(self):
        self.SYSTEM_PROMPT = Model_Config.SYSTEM_PROMPT
        self.MODEL_NAME = Model_Config.MODEL_NAME
        self.FILE_1_NAME_XLSX = Model_Config.FILE_1_NAME_XLSX
        self.EXAMPLE_1_RESPONSE = Model_Config.EXAMPLE_1_RESPONSE
        self.EXAMPLE_2_RESPONSE = Model_Config.EXAMPLE_2_RESPONSE
        self.EXAMPLE_3_RESPONSE = Model_Config.EXAMPLE_3_RESPONSE
    @staticmethod
    def read_file(file_name:str)->pd.DataFrame:
        if file_name.endswith('.xlsx'):
            df = pd.read_excel(file_name)
        elif file_name.endswith('.csv'):
            df = pd.read_csv(file_name)
        elif file_name.endswith('.json'):
            df = pd.read_json(file_name)
        return df
    @staticmethod
    def generate_prompt(parameter_list:list)->str: # inCODE 1.04
        parameters = ' '.join(parameter_list)
        prompt_text = f"""
                            Prompt template {parameters} prompt template
                        """
        return prompt_text
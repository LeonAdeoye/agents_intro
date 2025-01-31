import os
import platform
import torch


def get_info():
    print(torch.__version__)
    pythonVersion = platform.python_version()
    finalVersion = "Python version: " + pythonVersion
    print(f'{finalVersion}')
    print(f'OpenAI API Key = {os.environ["OPENAI_API_KEY"]}')

import pandas as pd
import numpy as np
import seaborn as sns
import os
import sys
import datetime
import time
import json
import requests
import re
import random
import string
import warnings
import logging


# folderpath = os.getcwd() + "/datasets/"
# files = os.listdir(folderpath)
# xlsx_files = [file for file in files if file.endswith('.xlsx')]

# if xlsx_files:
#     file = xlsx_files[0]
# else:
#     print("No .xlsx files found in the folder.")
# df = pd.read_excel(folderpath + file).iloc[2:].fillna(0).reset_index(drop=True)
# for i in range(2, len(df.iloc[0, :])-2, 3):
#     # print(i)
#     df.iloc[0, i+1] = df.iloc[0, i]
#     df.iloc[0, i+2] = df.iloc[0, i]
# # df = df[(df != 0).all(axis=1)]
# df.iloc[[1, 0]] = df.iloc[[0, 1]]
# names = []
# for i in range(df.iloc[0, :].shape[0]):
#     names.append(df.iloc[0, i] + ' ' + str(df.iloc[1, i]))
# df.columns = names
# df = df.drop([0, 1]).reset_index(drop=True)

# import certifi
# import certifi
# print(certifi.where())
# with open(certifi.where(), 'r') as cert_file:
#     certificate_content = cert_file.read()
#     print(certificate_content)
# os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

from openai import OpenAI

session = requests.Session()
session.verify = True

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
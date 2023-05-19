import os
from twilio.rest import Client
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from tqdm import tqdm
from datetime import datetime
from utils import request_wapi,get_forecast,create_df,send_message,get_date


TWILIO_ACCOUNT_SID =os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN =os.environ["TWILIO_AUTH_TOKEN"]
PHONE_NUMBER ="+12545705477"
query = 'Córdoba'
api_key = "8ab276a6f3f24bc8987184908231805"

input_date= get_date()
response = request_wapi(api_key,query)

datos = []

for i in tqdm(range(24),colour = 'green'):

    datos.append(get_forecast(response,i))


df_rain = create_df(datos)

# Send Message
message_id = send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df_rain,query)


print('Mensaje Enviado con exito ' + message_id)

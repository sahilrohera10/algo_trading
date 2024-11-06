
from dhanhq import dhanhq # type: ignore
from dotenv import load_dotenv # type: ignore
import pandas as pd # type: ignore
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
access_token = os.getenv("ACCESS_TOKEN")

dhan = dhanhq(client_id,access_token)


class Portfolio : 

    def get_positions(dhan):
        position_data = dhan.get_positions()
        return position_data
    
    def get_holding(dhan):
        holding_data = dhan.get_holdings()
        return holding_data
 


position_data = Portfolio.get_positions(dhan)
print("position_data => ", position_data)

holding_data = Portfolio.get_holding(dhan)
print("holding_data => ", holding_data)




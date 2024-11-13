
from dhanhq import dhanhq # type: ignore
from dotenv import load_dotenv # type: ignore
import pandas as pd # type: ignore
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
access_token = os.getenv("ACCESS_TOKEN")

dhan = dhanhq(client_id,access_token)


def get_historical_data(dhan,symbol, exchange_segment, instrument_type, from_date, to_date):
    historical_data = dhan.historical_daily_data(
        symbol=symbol,
        exchange_segment=exchange_segment,
        instrument_type=instrument_type,
        from_date=from_date,
        to_date=to_date
    )
    print(historical_data)
 


symbol_list=['TCS','ITC']

for symbol in symbol_list:
    exchange_segment='NSC_EQ',
    instrument_type='EQUITY',
    from_date='2022-01-08',
    to_date='2022-02-08'
    get_historical_data(dhan,symbol,exchange_segment, instrument_type, from_date, to_date)

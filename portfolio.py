
from dhanhq import dhanhq # type: ignore
from dotenv import load_dotenv # type: ignore
import pandas as pd # type: ignore
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
access_token = os.getenv("ACCESS_TOKEN")

dhan = dhanhq(client_id,access_token)

def get_positions(dhan):
    position_data = dhan.get_positions()
    return position_data
    
def get_holding(dhan):
    holding_data = dhan.get_holdings()
    return holding_data



# util functions for place order 
def get_exchange(dhan, exchange):
    if exchange == "BSE":
        return dhan.BSE
    elif exchange == "MCX":
        return dhan.MCX
    elif exchange == "NSE":
        return dhan.NSE

def get_side(dhan, side):
    if side == "BUY":
        return dhan.BUY
    if side == "SELL":
        return dhan.SELL
    
def get_order_type(dhan, order_type):
    if order_type == "MARKET":
        return dhan.MARKET
    if order_type == "LIMIT":
        return dhan.LIMIT

# Place an order for Equity Cash
def place_my_order(dhan, symbol, exchange, side, quantity, order_type, price):

    exchange_segment = get_exchange(dhan, exchange)
    transaction_type = get_side(dhan, side)
    order_type_1 = get_order_type(dhan, order_type)

    order_id = dhan.place_order(
        security_id=symbol,            # HDFC Bank
        exchange_segment=exchange_segment,
        transaction_type=transaction_type,
        quantity=quantity,
        order_type=order_type_1,
        product_type=dhan.INTRA,
        price=price
    )
    return order_id


def get_my_orders(dhan):
    orders = dhan.get_order_list()
    positions = pd.DataFrame(orders["data"])
    print(positions)
    return


def get_instrument_token():
    df = pd.read_csv('api-scrip-master.csv')
    data_dict={}
    for index,row in df.iterrows():
        trading_symbol= row['SEM_TRADING_SYMBOL']
        exm_exch_id= row['SEM_EXM_EXCH_ID']
        if trading_symbol not in data_dict:
            data_dict[trading_symbol]={}
        data_dict[trading_symbol][exm_exch_id]=row.to_dict()

    return data_dict

# tokem_dict=get_instrument_token()
# print(tokem_dict['HDFCBANK']['BSE']['SEM_SMST_SECURITY_ID'])


def get_symbol_name(symbol, expiry, strike, strike_type):
    instrument = f'{symbol}-{expiry}-{str(strike)}-{strike_type}'
    return instrument


security_id='1333',            # HDFC Bank
exchange_segment="NSE",
transaction_type="BUY",
quantity=10,
order_type="MARKET",
price=0

order_id = place_my_order(dhan, security_id, exchange_segment, transaction_type, quantity, order_type, price)
print(order_id)

# position_data = get_positions(dhan)
# print("position_data => ", position_data)

# holding_data = get_holding(dhan)
# print("holding_data => ", holding_data)





# fetching my all orders 
# get_my_orders(dhan)




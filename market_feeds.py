
from dhanhq import marketfeed
from dotenv import load_dotenv # type: ignore
import pandas as pd # type: ignore
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
access_token = os.getenv("ACCESS_TOKEN")

  
instruments = [(marketfeed.NSE, "1333", marketfeed.Ticker),   # Ticker - Ticker Data
    (marketfeed.NSE, "1333", marketfeed.Quote),     # Quote - Quote Data
    (marketfeed.NSE, "1333", marketfeed.Full),      # Full - Full Packet
    (marketfeed.NSE, "11915", marketfeed.Ticker),
    (marketfeed.NSE, "11915", marketfeed.Full)]

version = "v2"          # Mention Version and set to latest version 'v2'

# In case subscription_type is left as blank, by default Ticker mode will be subscribed.

try:
    data = marketfeed.DhanFeed(client_id, access_token, instruments, version)
    while True:
        data.run_forever()
        response = data.get_data()
        print(response)

except Exception as e:
    print(e)

# Close Connection
data.disconnect()

# Subscribe instruments while connection is open
sub_instruments = [(marketfeed.NSE, "14436", marketfeed.Ticker)]

data.subscribe_symbols(sub_instruments)

# Unsubscribe instruments which are already active on connection
unsub_instruments = [(marketfeed.NSE, "1333", 16)]

data.unsubscribe_symbols(unsub_instruments)
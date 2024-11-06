# Algo Trading Platform

This project is a Python-based algorithmic trading platform that connects to the Dhan API to manage and trade stocks. The platform is designed to support advanced trading algorithms on historical data and, based on the algorithms’ outputs, send real-time buy/sell signals to execute trades.

## Features

- **Portfolio Management**: Retrieve and manage trading positions and holdings.
- **Algorithmic Trading** (Planned): Run customizable trading algorithms on historical data to identify potential trade opportunities.
- **Automated Signals** (Planned): Based on algorithmic outputs, automatically send buy/sell signals to Dhan to manage holdings.
- **Environment Variable Management**: Securely load sensitive credentials from a `.env` file.

## Requirements

- Python 3.x
- [Dhan API](https://dhanhq.co/) credentials (client ID and access token)

## Installation

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd algo-trading
   Install Dependencies
   ```

```bash
pip install -r requirements.txt
```

Set Up Environment Variables

Create a .env file in the project directory and add your Dhan API credentials:

```bash
CLIENT_ID="your_client_id"
ACCESS_TOKEN="your_access_token"
```

## Usage

The initial implementation provides methods to access and print portfolio positions and holdings. The project will eventually support running trading algorithms and executing trades based on generated signals.

## Run the Script

```bash
python portfolio.py
```

Current Output The script currently prints out the user's trading positions and holdings.

## Code Overview

1. Environment Loading: Uses dotenv to load credentials from the .env file.
2. Portfolio Class: Currently provides methods to access portfolio data:
3. get_positions: Retrieves and displays position data from Dhan.
4. get_holding: Retrieves and displays holding data from Dhan.
5. Future Additions: The platform will incorporate algorithmic trading models, with the ability to analyze historical data and automatically execute trades based on model signals.

## Example Output

After running the script, you should see output like:

position_data => { ... } # Displays position data
holding_data => { ... } # Displays holding data

## Roadmap

1. Data Analysis Module: Integrate historical data analysis to train and test trading algorithms.
2. Signal Generation: Implement various trading algorithms that generate buy/sell signals based on historical and real-time data.
3. Automated Trade Execution: Enable automated trade execution based on algorithmic signals, directly interacting with the Dhan API.

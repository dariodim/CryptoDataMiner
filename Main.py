import pandas as pd
import datetime as datetime
import Libraries.CoinGecko as CoinGecko_API

# Paramenters
NumberOfInstruments = 50

# Sorting
SortingMethod = 'market_cap_desc'

# Parse list of instruments from CoinGecko by Market Cap (Highest to Lowest)
CoinList_CALL = 'https://api.coingecko.com/api/v3/coins?order=?' + SortingMethod
CoinList = pd.DataFrame(CoinGecko_API.CoingeckoAPI(CoinList_CALL).get_coingecko_data())

MainData = pd.DataFrame(columns=['Date', 'Time', 'Id', 'Name', 'Symbol', 'Description', 'GenesisDate'])

# Loop through top instruments
for i in range(0,NumberOfInstruments-1):

    # Parse full information about instrument
    CoinInformation_CALL = 'https://api.coingecko.com//api/v3/coins/' + CoinList['id'][i]
    CoinInformation = CoinGecko_API.CoingeckoAPI(CoinInformation_CALL).get_coingecko_data()

    # Id of instrument
    Id = CoinInformation['id']

    # Name of instrument
    Name = CoinInformation['name']

    # Symbol of instrument
    Symbol = CoinInformation['symbol']

    # Description of instrument
    Description = CoinInformation['description']['en']

    # Genesis of instrument
    GenesisDate = CoinInformation['genesis_date']

    # Add data to Main Table
    MainData.loc[len(MainData)+1] = [pd.datetime.now().strftime("%Y-%m-%d"), pd.datetime.now().strftime("%H:%M:%S"), Id, Name, Symbol, Description, GenesisDate]

print(MainData)
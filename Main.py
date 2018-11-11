import pandas as pd
import Libraries.CoinGecko as CoinGecko_API

NumberOfInstruments = 50

# Parse list of coins from CoinGecko by Market Cap (Highest to Lowest)
CoinList_CALL = 'https://api.coingecko.com/api/v3/coins?order=market_cap_desc?'
CoinList = pd.DataFrame(CoinGecko_API.CoingeckoAPI(CoinList_CALL).get_coingecko_data())

# Parse full information about bitcoin
CoinInformation_CALL = 'https://api.coingecko.com//api/v3/coins/' + CoinList['id'][0]
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
print('A')
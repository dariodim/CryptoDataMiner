import pandas as pd
import Libraries.CoinGecko as CoinGecko_API

# Parse list of coins from CoinGecko
CoinList_CALL = 'https://api.coingecko.com/api/v3/coins/list'
CoinList = pd.DataFrame(CoinGecko_API.CoingeckoAPI(CoinList_CALL).get_coingecko_data())

# Parse full information about bitcoin
CoinInformation_CALL = 'https://api.coingecko.com//api/v3/coins/bitcoin'
CoinInformation = CoinGecko_API.CoingeckoAPI(CoinInformation_CALL).get_coingecko_data()

#CoinInformation = pd.DataFrame(CoinGecko_API.CoingeckoAPI(CoinInformation_CALL).get_coingecko_data())
print(type(CoinInformation))
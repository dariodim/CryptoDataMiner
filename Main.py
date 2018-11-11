import json
import pandas as pd
import Libraries.CoinGecko as coin

coinList = coin.CoingeckoAPI('https://api.coingecko.com/api/v3/coins/list')

print(pd.DataFrame(coinList.get_coingecko_data()))
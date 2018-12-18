import pandas as pd
import datetime as datetime
import Libraries.CoinGecko as CoinGecko_API
import Libraries.ConfigReader as ConfigurationReader
import Libraries.DBConnector as DBInteraction

# Import Config Parameters
ConfigData = ConfigurationReader.ConfigReader('Config.json').read_config()

# Connect to Database & Pass Instructions
DBInteraction.PostgreSQL().ConnectToDB(ConfigData['PostgreSQL']['user'], ConfigData['PostgreSQL']['password'], ConfigData['PostgreSQL']['host'], ConfigData['PostgreSQL']['port'], ConfigData['PostgreSQL']['database'], """SELECT * FROM "Schema"."Securities";""")



# Paramenters
NumberOfInstruments = 10

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

def SQL_INSERT_STATEMENT_FROM_DATAFRAME(SOURCE, TARGET):
    sql_texts = []
    for index, row in SOURCE.iterrows():       
        sql_texts.append('INSERT INTO '+TARGET+' ('+ str(', '.join(SOURCE.columns))+ ') VALUES '+ str(tuple(row.values)))
    
    return sql_texts
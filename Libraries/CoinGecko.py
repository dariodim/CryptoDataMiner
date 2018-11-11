import urllib.request, urllib.parse, urllib.error
import ssl
import json

class CoingeckoAPI:
    # Receives the API URL as an argument during the object construction.

    def __init__(self, url):
        self.url = url

    def get_coingecko_data(self):
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        #Making the API call, decoding the data and loading them into json
        request = urllib.request.Request(self.url)
        
        #Adding user agent to bypass 403 error.
        request.add_header('User-Agent',"Mozilla/5.0")
        uh = urllib.request.urlopen(request)
        data = uh.read().decode()

        return json.loads(data)
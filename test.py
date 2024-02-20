import urllib.request
csv_url = 'https://data.cityofnewyork.us/resource/uip8-fykc.csv'
file_path = 'data/file.csv'
urllib.request.urlretrieve(csv_url, file_path)
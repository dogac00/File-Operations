from urllib import request

url = 'sample.csv'

def download_data(csv_url): # download data function
  response = request.urlopen(csv_url) # open url
  csv = response.read() # read data
  csv_str = str(csv) # convert to string
  lines = csv_str.split("\\n") # split the string into lines
  for line in lines:
    print(line) # print each line

download_data(url)

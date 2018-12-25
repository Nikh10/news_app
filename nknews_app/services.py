import requests


url = ('https://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=20ec45ccad044842bbf01848227efed4')



def populate_data():
    response = requests.get(url)
    return response.json()


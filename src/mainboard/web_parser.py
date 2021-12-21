import requests
from bs4 import BeautifulSoup

url = 'http://192.168.0.247/'

def read_data():
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('body')
        
        print(title.get_text())
        a = title.get_text()
        
        if (a[0] == '1'):
            return 1
        
        elif (a[0] == '0'):
            return 0
            
    else : 
        print(response.status_code)
        

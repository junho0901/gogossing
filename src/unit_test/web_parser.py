import requests
from bs4 import BeautifulSoup

url = 'http://192.168.144.210/'

def read_data():
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('body')
        print(title.get_text())
        a = title.get_text()
        
        if (a[0] == '0'):
            print("성공")
    else : 
        print(response.status_code)

   
def test_data():
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('body')
        print(title.get_text())
        a = int(title.get_text())
        
        return a

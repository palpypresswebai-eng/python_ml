'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to 
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.

'''

'''

https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/
'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'

]

def fetch_content(url):
    respones = requests.get(url)
    soup = BeautifulSoup(respones.content,'html.parser')
    print(f"fetched {len(soup.text)} and your url")

thredes= []

for link in urls:
    threde = threading.Thread(target=fetch_content,args=(link,))
    thredes.append(threde)
    threde.start()

for new_result in thredes:
    new_result.join()

print("All web pages fetched")

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# 定义爬取的URL
search_url = 'https://www.vodtw.la/book/2826/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}
# 发送HTTP请求获取页面内容
response = requests.get(search_url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    list = soup.find_all('div', class_='section-box')
    list2 = list[1].find('ul', class_='section-list fix').find_all('li')
    for item in tqdm(list2):
        print(item)
        print(item.find('a').get('href'))

from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver

base_url = "https://www.vodtw.la"
suffix_url = "/book/2826/chapter/dir_1.html"
search_url = base_url + suffix_url

# 获取所有章节页面的链接
chapter_links = []
next_page_links = []

with open('agent.txt', 'r') as f:
    agent = f.read()
headers = {
    'User-Agent': agent
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')

driver = webdriver.Chrome(options=chrome_options)
driver.get(search_url)
driver.implicitly_wait(10)  # 适当调整等待时间

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# 找到<select>标签
select_tag = soup.find('span', class_='middle')

# 找到所有<option>标签
option_tags = select_tag.find_all('option')
# 遍历并打印每个<option>标签的值
for option in option_tags:
    # print(option.text)  # 输出<option>标签的文本内容
    # print(option['value'])  # 输出<option>标签的'value'属性值
    next_page_links.append(base_url + option['value'])

for next_page_link in next_page_links:
    driver.get(next_page_link)
    driver.implicitly_wait(20)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    list = soup.find_all('div', class_='section-box')[1].find('ul', class_='section-list fix').find_all('li')
    for item in tqdm(list):
        chapter_links.append(base_url + item.find('a').get('href'))


def scrape_chapter(chapter_link):
    driver.get(chapter_link)
    driver.implicitly_wait(20)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    #     <div class="content" id="content">
    content = soup.find('div', id='content').get_text(separator='\n')
    print(content)
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(content)
        f.write('\n')
        f.flush()  # 刷新缓冲

    i = 1
    if "本章未完，点击下一章继续阅读" in content:
        next_page_link = chapter_link.replace(".html", "_" + str(i) + ".html")
        scrape_chapter(next_page_link)


# 遍历每个章节页面链接并获取内容
for chapter_link in tqdm(chapter_links):
    scrape_chapter(chapter_link)

driver.quit()

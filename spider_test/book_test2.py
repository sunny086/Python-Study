from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver

base_url = "https://www.vodtw.la"
suffix_url = "/book/2826/chapter/dir_1.html"
search_url = base_url + suffix_url

with open('agent.txt', 'r') as f:
    agent = f.read()
headers = {
    'User-Agent': agent
}
# 创建Chrome浏览器实例，并将请求头添加到浏览器中
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 无界面模式，可根据需要调整
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
# chrome_options.add_argument(f'--cookie="{headers["Cookie"]}"')

# 创建Chrome浏览器实例
driver = webdriver.Chrome(options=chrome_options)

driver.get(search_url)
driver.implicitly_wait(20)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# 找到<select>标签
select_tag = soup.find('span', class_='middle')

# 找到所有<option>标签
option_tags = select_tag.find_all('option')


# 获取所有章节页面的链接
chapter_links = []

# 遍历并打印每个<option>标签的值
for option in option_tags:
    print(option.text)  # 输出<option>标签的文本内容
    print(option['value'])  # 输出<option>标签的'value'属性值

# div section-box 下级 ul section-list fix 再下级 li标签中包含了部分章节的目录名称和每一章节的链接
list = soup.find_all('div', class_='section-box')[1].find('ul', class_='section-list fix').find_all('li')
for item in tqdm(list):
    print(item)
    print(item.find('a').get('href'))

driver.quit()

from selenium import webdriver
from bs4 import BeautifulSoup

# 读取文件agent.txt，获取请求头
with open('agent.txt', 'r') as f:
    agent = f.read()
# 读取文件cookie.txt，获取请求头
with open('cookie.txt', 'r') as f:
    cookie = f.read()

# 设置请求头，包括 Cookie 和 User-Agent
headers = {
    'User-Agent': agent,
    'Cookie': cookie
}

# 创建Chrome浏览器实例，并将请求头添加到浏览器中
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # 无界面模式，可根据需要调整
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
# chrome_options.add_argument(f'--cookie="{headers["Cookie"]}"')

# 创建Chrome浏览器实例
driver = webdriver.Chrome(options=chrome_options)

# 定义爬取的URL
base_url = "https://www.zhipin.com"
# suffix_url = "/web/geek/job-recommend"
suffix_url = "/web/geek/job?query=&city=101220100&position=100101"
search_url = base_url + suffix_url

# 发送HTTP请求获取页面内容
driver.get(search_url)

# 使用Selenium等待页面加载完成（你可以根据页面实际情况调整等待时间）
driver.implicitly_wait(10000)

# 获取页面内容
page_source = driver.page_source

# 使用Beautiful Soup解析页面
soup = BeautifulSoup(page_source, 'html.parser')
# 找到招聘信息的容器
job_list = soup.find_all('li', class_='job-card-wrapper')
for job in job_list:
    job_title = job.find('span', class_='job-name').text
    print("职位名称:", job_title)
    print("\n")
# 关闭浏览器
driver.quit()

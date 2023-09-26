import requests
from bs4 import BeautifulSoup

# 定义爬取的URL
base_url = "https://www.zhipin.com"
suffix_url = "/web/geek/job-recommend"
# suffix_url = "/web/geek/job?query=Java&city=101190100&position=100101&page=2"
search_url = base_url + suffix_url

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}
# 发送HTTP请求获取页面内容
response = requests.get(search_url, headers=headers)
if response.status_code == 200:
    # 打印页面内容
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到招聘信息的容器
    job_list = soup.find_all('div', class_='job-primary')

    for job in job_list:
        # 提取招聘信息
        job_title = job.find('div', class_='job-title').text.strip()
        company = job.find('div', class_='company-text').a.text.strip()
        salary = job.find('span', class_='red').text.strip()

        # 打印招聘信息
        print("职位:", job_title)
        print("公司:", company)
        print("薪水:", salary)
        print("=" * 30)
else:
    print("无法获取页面内容")

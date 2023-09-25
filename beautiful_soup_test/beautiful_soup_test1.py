from bs4 import BeautifulSoup

# 示例HTML文档
html_doc = """
<html>
<head>
    <title>示例页面</title>
</head>
<body>
    <h1>这是一个标题</h1>
    <p>这是一个段落。</p>
    <ul>
        <li>列表项1</li>
        <li>列表项2</li>
        <li>列表项3</li>
    </ul>
</body>
</html>
"""

# 创建Beautiful Soup对象
soup = BeautifulSoup(html_doc, 'html.parser')

# 通过标签名获取元素
title = soup.title
print("标题标签:", title)
print("标题文本:", title.string)

# 通过标签名和属性获取元素
h1 = soup.find('h1')
print("H1标签:", h1)
print("H1文本:", h1.text)

# 获取段落文本
p = soup.find('p')
print("段落文本:", p.text)

# 遍历列表项
ul = soup.find('ul')
li_items = ul.find_all('li')
print("列表项:")
for li in li_items:
    print(li.text)

# import requests
#
# query = "巴莉甜甜"
# url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1&no_html=1"
#
# response = requests.get(url)
# data = response.json()
#
# print("抽象：", data.get("Abstract"))
# print("相关话题：", data.get("RelatedTopics"))


# search.py

from ddgs import DDGS

results = DDGS().text("巴莉甜甜", max_results=10)
print(results)

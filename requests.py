import requests
url= "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
print("天气信息：")
print(data)
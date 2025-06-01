import requests

#東京都が主催者等であるイベント情報の一覧
API_URL  = "https://api.data.metro.tokyo.lg.jp/v1/Event?limit=100"

params = {
    "limit":"100" #最大取得レコード数
}

#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()

print(data)
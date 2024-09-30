import requests
from bs4 import BeautifulSoup

# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get('https://atcoder.jp/contests/abc368/tasks/abc368_a')

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(res.text, 'html.parser')

## 入力例2個：10 入力例が1,3, 出力例が2,4
## 入力例3個：14 入力例が1,3,5 出力例が2,4,6

pre_contents = soup.find_all('pre')

input_sample = [pre_contents[1].text, pre_contents[3].text]
output_sample = [pre_contents[2].text, pre_contents[4].text]

print(input_sample)
print(output_sample)

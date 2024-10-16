import requests
from bs4 import BeautifulSoup

url = 'https://2023ntcu.ntcu.edu.tw/'
html = requests.get(url)
html.encoding = "utf-8"  # Set encoding to UTF-8
soup = BeautifulSoup(html.text, 'html.parser')  # Use 'html.text' instead of 'response.text'

print(soup.prettify())  # Print the formatted HTML
count = 0
keyword = '臺中'

# Search for the keyword in all stripped strings on the webpage
for text in soup.stripped_strings:
    if keyword in text:
        count += 1
        print(f"找到關鍵詞 '{keyword}'. 當前計數: {count}")

print(f"關鍵詞 '{keyword}' 共出現 {count} 次")

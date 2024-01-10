import mechanicalsoup
import bs4
import requests

browser = mechanicalsoup.StatefulBrowser()

browser.open("https://www.gsa-spark.com/speedtest/dbe63a9c-d8b0-4623-8789-c6dab8696654")


browser.select_form()
res = requests.get('https://www.gsa-spark.com/speedtest/dbe63a9c-d8b0-4623-8789-c6dab8696654')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
num1 = soup.select('#number1')
num1 = num1[0].text.strip()
num2 = soup.select('#number2')
num2 = num2[0].text.strip()

total = int(num1) + int(num2)
print(total)

browser["answer"] = total

response = browser.submit_selected()

print(response.text)





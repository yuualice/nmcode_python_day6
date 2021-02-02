import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

os.system("clear")
url = "https://www.iban.com/currency-codes"

country_list = []

def scrap_url():
    link = requests.get(url)
    soup = BeautifulSoup(link.text, "html.parser")
    rows = soup.find("tbody").find_all("tr")
    for row in rows:
        data = row.find_all("td")
        country = data[0].text
        currency = data[1].text
        code = data[2].text
        num = data[3].text
        if currency != "No universal currency":
            country_list.append((country, currency, code, num))

country = []
currency = []
code = []
num = []

def extract_url():
    for list in country_list:
        country.append(list[0])
        currency.append(list[1])
        code.append(list[2])
        num.append(list[3])
    for index in range(len(country)):
        print(f'# {index} {country[index].capitalize()}')

scrap_url()
extract_url()

url_transfer = "https://transferwise.com/gb/currency-converter/"

def ask_first_country():
  try:
    answer_1 = int(input("Where are you from? Please choose country by number\n#: "))
    if 0 < answer_1 < len(country_list):
      print(country[answer_1])
      return answer_1
    else:
      print("Choose a number from the list.")
      ask_first_country()
  except ValueError:
    print("That is not a number.")
    ask_first_country()

def ask_second_country():
  try:
    answer_2 = int(input("#:\n"))
    if 0 < answer_2 < len(country_list):
      print(country[answer_2])
      return answer_2
    else:
      print("Choose a number from the list.")
      ask_second_country()
  except:
    print("That is not a number.")
    ask_second_country()

input_1 = ask_first_country()
input_2 = ask_second_country()

def currency_convert (input_1, input_2):
  input_1 = int(input_1)
  input_2 = int(input_2)
  print(f"\nHow many {code[input_1]} do you want to convert to {code[input_2]}?")
  try:
    input_3 = input("\n#:")
    url_2 = f"https://transferwise.com/gb/currency-converter/{str(code[input_1])}-to-{str(code[input_2])}-rate?amount={str(input_3)}"
    link_url = requests.get(url_2)
    soup_url = BeautifulSoup(link_url.text, "html.parser")
    extract = soup_url.find("span", {"class": "text-success"}).string
    input_3 = int(input_3)
    converted = format_currency(float(extract) * input_3, code[input_2], locale="ko_KR")
    print(f"{code[input_1]}{input_3} is {converted}")

  except AttributeError:
    print("That wasn't a number.")
    return currency_convert(input_1, input_2)

output_3 = currency_convert(input_1,input_2)

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_current_weather_condition():
    city = "Athens"

    # creating url and requests instance
    url = "https://www.google.com/search?q=" + "weather+" + city
    html = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}).content

    # getting raw data
    soup = BeautifulSoup(html, "html.parser")

    period = soup.find('div', attrs={'class': 'wob_dts'}).text
    description = soup.find('div', attrs={'class': 'wob_dcp'}).text
    temperature = soup.find('span', attrs={'class': 'wob_t q8U8x'}).text
    print(f'"Time:{period}, Sky Description: {description}, Temperature: {temperature}"')


def get_weather_data_for_next_days():
    # creating url and requests instance
    url = "https://weather.com/weather/tenday/l/Larissa+Thessaly+Greece?canonicalCityId=d013f501a2e052fd4838d86aeff4a0cc7f7c8a6b147132a156284363357aea4f"
    html = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}).content

    # getting raw data
    soup = BeautifulSoup(html, "html.parser")

    days = soup.find_all('details',
                         attrs={'class': 'DaypartDetails--DayPartDetail--n5F8Y Disclosure--themeList--vEbAF'})

    period = [item.find('h2', attrs={'class': 'DetailsSummary--daypartName--CcVUz'}).text for item in days]
    description = [item.find('title').text for item in days]
    temperature = [item.find('div', attrs={'class': 'DetailsSummary--temperature--YGmQ5'}).text for item in days]

    df = pd.DataFrame({"Period": period, "Short Description": description, "Temperature": temperature})
    df.to_csv("WeatherData.csv")


get_current_weather_condition()
get_weather_data_for_next_days()

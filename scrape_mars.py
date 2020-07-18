import pandas as pd
pd.options.display.max_colwidth = 100
import datetime
import requests
import time
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path)


def scrape_info():

    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)
    time.sleep(1)
    nasa_html = browser.html
    nasa_soup = BeautifulSoup(nasa_html, 'html.parser')
    news_list = nasa_soup.find('ul', class_='item_list')
    first_item = news_list.find('li', class_='slide')


    nasa_headline = first_item.find('div', class_='content_title').text

    nasa_para1 = first_item.find('div', class_='article_teaser_body').text

    print(f'** The latest NASA Headline is:** {nasa_headline}')
    print(f'** NASA Headline 1st Paragraph:** {nasa_para1}')

    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    print(f' Featured Image URL: {featured_image_url}')

    weather_url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(weather_url)
    time.sleep(1)

    mars_weather_html = browser.html
    soup = BeautifulSoup(mars_weather_html, 'html.parser')

    weather_mars = []
    for content in contents:
        tweets = soup.find_all('div', attrs={'data-testid':'tweet'})
        weather_mars.append(tweets)

    tweets = [y.text for y in tweet]

    raw_tweets = pd.DataFrame({'tweet':tweets})
    raw_tweets

    weather_tweets = raw_tweets[raw_tweets.tweet.str.contains("InSight")]
    weather_tweets

    weather_tweets['weather'] = raw_tweets['tweet'].str.replace('.*(?=InSight)', '', regex=True)
    weather_tweets = pd.DataFrame(weather_tweets)
    weather_tweets

    weather_tweets['date'] = pd.to_datetime(weather_tweets['weather'].apply(lambda x: re.search('\((\d{4}-\d{2}-\d{2})\)', x).group(1)))
    weather_tweets

    pd.options.display.max_colwidth = 200
    latest_weather = weather_tweets[weather_tweets.date == weather_tweets.date.max()].weather.to_frame()
    print(f'The latest weather on Mars is: {latest_weather}')

    space_facts_url = "https://space-facts.com/mars/"
    mars_profile_profile = pd.read_html(space_facts_url)
    table[0]
    table[0].columns = ["Facts", "Value"]
    table[0]

    HTML_table_string = table[0].to_html()
    HTML_table_string = HTML_table_string.replace("\n","")
    HTML_table_string

    mars_hemisphere_image_urls = []

    url = ('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')

    print(soup.prettify())

    for i in range(1,9,2):

        hemi_dict = {}

        browser.visit(url)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        hemisphere_name_link = soup.find_all('a', class_='product-item')
        hemisphere_name = hemisphere_name_link[i].text.strip('Enhanced')

        hemisphere_detail_links = browser.find_by_css('a.product-item')

        hemisphere_detail_links[i].click()

        time.sleep(1)

        browser.find_link_by_text('Sample').first.click()

        time.sleep(1)

        browser.windows.current = browser.windows[-1]
        hemi_img_html = browser.html
        browser.windows.current = browser.windows[0]
        browser.windows[-1].close()

        soup = BeautifulSoup(hemi_img_html, 'html.parser')
        image_path = soup.find('img')['src']

        print(hemisphere_name)
        hemi_dict['title'] = hemisphere_name.strip()

        print(image_path)
        hemi_dict['img_url'] = image_path

        mars_hemisphere_image_urls.append(hemi_dict)

    mars_data["hemisphere_imgages"] = mars_hemisphere_image_dict

    browser.quit()

    return mars_data

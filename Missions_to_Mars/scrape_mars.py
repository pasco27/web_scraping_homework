# creating python script that is performing same functions as mission_to_mars.ipynb

import os
import json
import requests
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup

def scrape():
    mars_total_info = {}

#NASA News Section
    driverPath = '/usr/local/bin/chromedriver'
    
    
    # Setup configuration variables to enable Splinter to interact with browser
    # Deleted [0] fist instance of list here 
    executable_path = {'executable_path': driverPath}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # when this is loading - code moves on to grab html (too quickly) 
    # browser.html does not wait
    # --- spliter iselementpresent here --- 
    browser.is_text_present('splinter', wait_time=10)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('li', attrs = {'class':'slide'}).find('h3').text
    news_p = soup.find('div', class_= 'article_teaser_body').text

    # print(f"Title: {news_title}")
    # print(f"Teaser: {news_p}")

    # data to mars_info
    mars_total_info['news_title'] = news_title
    mars_total_info['news_p'] = news_p

    


#JPL Featured Image Section
    driverPath = '/usr/local/bin/chromedriver'
    # driverPath = !which chromedriver
    executable_path = {'executable_path': driverPath}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # when this is loading - code moves on to grab html (too quickly) 
    # browser.html does not wait
    # --- spliter iselementpresent here --- 
    browser.is_text_present('splinter', wait_time=10)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    images = soup.find_all('a', class_='fancybox')

    medium_image = []

    for image in images:
        photo = image['data-fancybox-href']
        medium_image.append(photo)
    
    featured_image_url = 'https://www.jpl.nasa.gov' + photo

    # print(featured_image_url)
     
    # data to mars_info
    mars_total_info['featured_image_url'] = featured_image_url
    
    browser.quit()

#Mars Facts Section 
    mars_facts_df = pd.read_html('https://space-facts.com/mars/')
    a = mars_facts_df[0]
    facts_in_html_a = a.to_html()
    b = mars_facts_df[1]
    facts_in_html_b = b.to_html()
    c = mars_facts_df[2]
    facts_in_html_c = c.to_html()
    # will have to work with HTML table here...

    print(facts_in_html_a) 
    print(b)
    print(c)

    # figured this out >>> going to have to figure out how to get this info into 1 nice table (?) on the html page
    #this is off to the side as well so make sure to style it appropriately on the page 
    browser.quit()

#Mars Hemispheres Section
    driverPath = '/usr/local/bin/chromedriver'
    # driverPath = !which chromedriver
    executable_path = {'executable_path': driverPath} # again removed [0]
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    browser.is_text_present('splinter', wait_time=10)

    mars_final = []

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemispheres = soup.find_all('div', class_='item')

    for hemisphere in hemispheres:
        title = hemisphere.find('h3').text

        image = hemisphere.find('img')['src']
        mars_final.append({'title':title, 'url': image})

    print(mars_final)

    #do I need theese throughtout?
    browser.quit()

    mars_total_info['hemisphere_image_urls'] = mars_final


    mars_total_info = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url,
        'mars_facts': html_table,
        'hemisphere_image_urls': mars_final
    }
    return mars_total_info
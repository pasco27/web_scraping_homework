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
    driverPath = !which chromedriver
    
    # Setup configuration variables to enable Splinter to interact with browser
    executable_path = {'executable_path': driverPath[0]}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

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
    driverPath = !which chromedriver
    executable_path = {'executable_path': driverPath[0]}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

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

    #going to have to figure out how to get this info into 1 nice table (?) on the html page
    #this is off to the side as well so make sure to style it appropriately on the page 


#Mars Hemispheres Section
    driverPath = !which chromedriver
    executable_path = {'executable_path': driverPath[0]}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    mars_final = []

    for hemisphere in hemispheres:
    title = hemisphere.find('h3').text
    link = hemisphere.find('a')['href']
    url = 'https://astrogeology.usgs.gov/'+link
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    dl = soup.find('div', class_='downloads')
    image = dl.find('a')['href']
    mars_final.append({'title':title, 'url': image})

    print(mars_final)

    #do I need theese throughtout?
    #browser.quit()

    mars_total_info['hemisphere_image_urls'] = mars_final


    mars_total_info = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url,
        'mars_facts': html_table,
        'hemisphere_image_urls': mars_final
    }
    return mars_total_info
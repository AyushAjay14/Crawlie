import re
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import get_mails
import sys
import clustter
import pandas as pd
import tldextract
import seleNium
import pdf_file
def main_func(url , depth , ss , cluster):

    d = int(0)
    # starting url. replace google with your own url.
    starting_url = str(url)
    ext = tldextract.extract(url)
    ss = int(ss)
    chrome_options = Options()
    chrome_options.add_argument('--log-level=1')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome( options=chrome_options)
    options = webdriver.ChromeOptions()
    options.headless = True


    #making new directory 
    get_mails.create_dir(ext.domain)


    f = open("Headers.txt" , "w+")

    
    # a queue of urls to be crawled
    unprocessed_urls = deque([starting_url])

    # set of already crawled urls for email
    processed_urls = set()

    # a set of fetched emails
    emails = set()

    #list of image links fetched
    images = []
    # process urls one by one from unprocessed_url queue until queue is empty
    while(len(unprocessed_urls) and d < int(depth)):

        # move next url from the queue to the set of processed urls
        url = unprocessed_urls.popleft()
        processed_urls.add(url)

        if(ss > 0):
            try:
                seleNium.screenshot(driver , url , ss)
                ss -=1
            except:
                pass
        # extract base url to resolve relative links
        parts = urlsplit(url)
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        # get url's content
        print("Crawling URL %s" % url)
        my_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","Accept-Encoding": "gzip, deflate" ,
        "permissions-policy": "interest-cohort=()"}
        try:
            response = requests.get(url , headers=my_headers)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            # ignore pages with errors and continue with next url
            continue

        f.write(str(response.headers) + '\n')
        # extract all email addresses and add them into the resulting set
        emails.update(get_mails.gemails(response))
        # create a beutiful soup for the html document
        soup = BeautifulSoup(response.text, 'lxml')

        imgs = soup.find_all('img')
        for img in imgs:
            if img.has_attr('src'):
                a = img['src']
                try:
                    if(a[0] == '/' and a[1] == '/'):
                        a = a[2:]
                except:
                    print(None)
                images.append(a)
        
        # Once this document is parsed and processed, now find and process all the anchors i.e. linked urls in this document
        for anchor in soup.find_all("a"):
            # extract link url from the anchor
            link = anchor.attrs["href"] if "href" in anchor.attrs else ''
            # resolve relative links (starting with /)
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            # add the new url to the queue if it was not in unprocessed list nor in processed list yet
            if not link in unprocessed_urls and not link in processed_urls:
                unprocessed_urls.append(link)
        d+=1
    
    df = pd.DataFrame(emails, columns=["Email"])
    df.to_csv('email.csv', index=False)
    df = pd.DataFrame(images, columns=["Image-Links"])
    df.to_csv('images.csv', index=False)
    df = pd.DataFrame(processed_urls, columns=["Crawled-Links"])
    df.to_csv('Crawled.csv', index=False)
    f.close()
    f = open("Headers.txt")
    data = f.read()
    pdf_file.text_to_pdf(data , "Headers.pdf")
    driver.quit()
    f.close()
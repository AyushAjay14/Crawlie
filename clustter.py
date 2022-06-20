import requests
import io
from PIL import Image
import time
import get_mails
import threading
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
def scroll_to_end(wd):
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  

def fetch_image_urls(query , max_links_to_fetch):
    

    get_mails.clust_dir("Google")
    max_links_to_fetch = int(max_links_to_fetch)
    chrome_options = Options()
    chrome_options.add_argument('--log-level=1')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    wd = webdriver.Chrome(ChromeDriverManager().install() , chrome_options=chrome_options)
    options = webdriver.ChromeOptions()
    options.headless = True


    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)
        
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(1)
            except Exception:
                continue

            # extract image urls    
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)
    thread_list = []

    for i, url in enumerate(image_urls):
        thread = threading.Thread(target=download_image, args=("Images/" , url , str(i)+ ".jpg"),)
        thread_list.append(thread)
        thread_list[i].start()
	    # download_image("imgs/", url, str(i) + ".jpg")
    for thread in thread_list:
        thread.join()
    wd.quit()
def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		with open(file_path, "wb") as f:
			image.save(f, "JPEG")

		print("Success")
	except Exception as e:
		print('FAILED -', e)
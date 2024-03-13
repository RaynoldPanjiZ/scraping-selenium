from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()

driver.get("https://www.haobo-imaging.com/products/?matchtype=p&placement=&device=c&network=g&campaignid=18134942583&adgroupid=139970487749&cid=617979234604&keyword=digital%20x%20ray%20detector%20panel&gclid=CjwKCAjwzo2mBhAUEiwAf7wjkib8y4GA6Xr6VG8m4bXppJD5DBToto-M3qcYL9ZEAf0AlBzVu3apBBoCr54QAvD_BwE/")


# body > div.container > section.web_main.page_main > div > section > div > div > div  > a
page = driver.find_element(By.CSS_SELECTOR, value='body > div.container > section.web_main.page_main > div > section > div > div > div > span').text
len_page = page.split(" ")[-1]

json_doc = {}
num = 0
start_time = time.time()
for ii in range(len_page):
    len_im = len(driver.find_elements(By.CSS_SELECTOR, value=f'body > div.container > section.web_main.page_main > div > section > div > ul > li'))
    print(len_im)
    for i in range(len_im):
    # for i, data in enumerate(datas):
        # print(data)
        data = driver.find_element(By.CSS_SELECTOR, value=f'body > div.container > section.web_main.page_main > div > section > div > ul > li:nth-child({i+1})')
        im_url = data.find_element(By.CSS_SELECTOR, 'figure > span > a')
        img = im_url.find_element(By.CSS_SELECTOR, 'img').get_attribute("src")
        # imgs.append(img)
        print(i,img)

        im_url.click()
        
        sub_datas = driver.find_elements(By.CSS_SELECTOR, value='body > div.container > section.web_main.page_main > div > section > section.product-intro > div > div:nth-child(2) > div.image-additional.swiper-container-horizontal > ul > li')
        sub_imgs = []
        for sub in sub_datas:
            img_sub = sub.find_element(By.CSS_SELECTOR, value='a').get_attribute("href")
            sub_imgs.append(img_sub)
            print('==>',img_sub)
        print()
        
        with open('./data.json','w') as file:
            sub_json = {num:{
                'img': img,
                'sub_img':sub_imgs
            }}
            json_doc.update(sub_json)
            json.dump(json_doc, file, indent = 4)
            num = num+1
            
        driver.back()
        # driver.execute_script("window.history.go(-1)")
        time.sleep(2)

    # body > div.container > section.web_main.page_main > div > section > div > div > div > a:nth-child(5)
    if ii == 0:
        driver.find_element(By.CSS_SELECTOR, value='body > div.container > section.web_main.page_main > div > section > div > div > div > a:nth-child(5)').click()
    elif ii >=0:
        driver.find_element(By.CSS_SELECTOR, value='body > div.container > section.web_main.page_main > div > section > div > div > div > a:nth-child(7)').click()
    time.sleep(2)
print()
print('elapsed : ', (time.time() - start_time))
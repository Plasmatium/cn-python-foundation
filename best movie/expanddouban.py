from selenium import webdriver
import time 

"""
url: the douban page we will get html from
loadmore: whether or not click load more on the bottom 
waittime: seconds the broswer will wait after intial load and 
""" 
def getHtml(url, loadmore = False, waittime = 2):
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)
    time.sleep(waittime)
    if loadmore:
        while True:
            try:
                next_button = browser.find_element_by_class_name("more")
                next_button.click()
                time.sleep(waittime)
            except:
                break
    html = browser.page_source
    browser.quit()
    return html

# for test
#url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,剧情,美国"
#html = getHtml(url)
#print(html) 

def newBrowser ():
    return webdriver.Chrome('chromedriver')

'''
def newBatch (urlList):
    browser = webdriver.Chrome('chromedriver')
    baseScript = """
    function spawnNew (url) {
        setTimeout(() => window.location = url, 0)
        setTimeout(() => window.stop(), 8000)
        window.open()
    }
    """
    time.sleep(10)
    for url in urlList:
        script = baseScript + f'\nspawnNew("{url}")'
        browser.execute_script(script)
        # browser.execute_script('window.open("about:blank")')
        browser.switch_to.window(browser.window_handles[-1])
    
    result = []
    for i in range(len(browser.window_handles) - 1): # len - 1 for last is 'about:blank'
        browser.switch_to.window(browser.window_handles[i])
        result.append(browser.page_source)
    
    return result
'''
                                       
'''
['https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,大陆',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,美国',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,香港',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,台湾',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,日本',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,韩国',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,英国',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,法国',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,德国',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,意大利',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,西班牙',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,印度',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,泰国',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,俄罗斯',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,伊朗',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,加拿大',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,澳大利亚',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,爱尔兰',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,瑞典',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,巴西',
 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,科幻,丹麦']
 '''
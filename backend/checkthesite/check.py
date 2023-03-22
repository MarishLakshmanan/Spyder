import time
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



# chrome_options.add_argument('--headless'-]ok

# chrome_options.add_argument('--disable-dev-shm-usage')
# baseUrl = 'http://localhost:5500/tester/1.html'
# url = 'http://localhost:5500/tester/1.html'
# baseUrl = 'http://books.toscrape.com/index.html'
# url = 'http://books.toscrape.com/index.html'


class Checker():

    # Anchor tag and html forms
    # should avoid going to other websites
    # avoid visiting same links again       
        


    def checkSite(self,url):
        self.driver.get(url)
        err = self.driver.get_log('browser')
        if(len(err)!=0):
            msg = ''
            
            for error in err:
                msg = msg+error['message']+", "

            self.driver.execute_script("elem = document.createElement('div');elem.innerHTML='<h4>"+msg+"</h4>';elem.style.cssText = 'position:absolute;top:0;left:0;background-color:rgba(0,0,0,.6);width:100%;height:100vh;color:white;display:flex;justify-content:center;align-items:center;z-index:7189237918;font-family:sans-serif;';document.getElementsByTagName('body')[0].appendChild(elem);")
            print("logError: "+url)
            filename =str(datetime.now().timestamp())
            # print(f'screenshots/{self.start}/{self.name}/{name}logError.png')
            if(not os.path.exists(f'screenshots/{self.name}/{self.start}')):
                os.mkdir(f'screenshots/{self.name}/{self.start}')
            self.driver.save_screenshot(f'screenshots/{self.name}/{self.start}/{filename}logError.png')

    def isVisited(self,url):
        for link in self.visited:
            if(link==url):
                return True
        return False

    def findTheSkip(slef,txt):
        txt = txt.split('/')
        count = 0
        tolink = []
        for link in txt:
            if(link==".."):
                count+=1
            else:
                tolink.append(link)
        return (count,"/".join(tolink))

    def splitandjoin(self,base,count,url):
        if(base[-1]=="/"):
            base = base[0:-1]
            print(base)
        base = base.split('/')
        base = base[0:-(count+1)]
        base = "/".join(base)
        return f'{base}/{url}'

    def checkLink(self,anchorTags,currentUrl):
        
        self.first
        self.checkSite(url=currentUrl)
        if(len(anchorTags)==0):
            return False
        for elem in anchorTags:
            url =elem.get("href") 
           
            try:
                if(url.find(self.baseUrl)):
                    
                    if(url.find('http')>-1):
                        print("other "+url)
                        continue
                    # print(currentUrl+" sdf "+url)
                    res = self.findTheSkip(txt=url)
                    url = self.splitandjoin(currentUrl,res[0],res[1])
            except Exception as e:
                print(e)
            if(self.isVisited(url=url)):
                continue  
            # res = requests.get(url)
            goodTogo = True
            try:
                self.driver.get(url)
            except Exception as e:
                print(e)
                goodTogo = False
            self.visited.append(url)
            # print(f'{url} status :{res.status_code}')
            # res.status.code==200
            if(goodTogo==True):
                self.first =False
                soup = BeautifulSoup(self.driver.page_source,'html.parser')
                anchorTags = soup.find_all('a')
                errorElem = self.checkLink(anchorTags,url)
                if(errorElem):
                    
                    href = errorElem.get('href')
                    self.driver.get(url)
                    self.driver.execute_script(f'''document.querySelectorAll("a[href='{href}']")[0].style.border="5px solid red"''')
                    filename =str(datetime.now().timestamp())
                    # print(f'screenshots/{self.start}/{self.name}/{filename}logError.png')
                    if(not os.path.exists(f'screenshots/{self.name}/{self.start}')):
                        os.mkdir(f'screenshots/{self.name}/{self.start}')
                    self.driver.save_screenshot(f'screenshots/{self.name}/{self.start}/{filename}.png')
                    
                    
            else:
                print("urlError: "+url)
                return elem
    def login(self,loginUrl,uselector,pselector,bselector,username,password,switchSelector):
        self.driver.get(loginUrl)
        if(not switchSelector==""):
            self.driver.find_element_by_css_selector(switchSelector).click()
        uelem = self.driver.find_element_by_css_selector(uselector)
        pelem = self.driver.find_element_by_css_selector(pselector)
        belem = self.driver.find_element_by_css_selector(bselector)
        uelem.send_keys(username)
        pelem.send_keys(password)
        belem.click()
        time.sleep(8)
        

    def checkTheSite(self,url,name,isAuth,auth={}):
        self.url = url
        self.baseUrl = url
        self.name = name
        self.d = DesiredCapabilities.CHROME
        self.d['loggingPrefs'] = { 'browser':'ALL' }
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path='./chromedriver',options=self.chrome_options,desired_capabilities=self.d) 

        if(isAuth):
            print("auth",auth)
            self.login(auth['loginurl'],auth['uid'],auth['pid'],auth['bid'],auth['username'],auth['password'],auth['sid'])

        # self.reqs = requests.get(self.url)
        self.driver.get(self.url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.anchorTags = self.soup.find_all('a') 

        self.start = f"{str(datetime.now().isoformat())} {url}".split(".")[0]
        
        self.visited = []
        self.first = True
        if(not os.path.exists(f'screenshots/{name}')):
            os.mkdir(f'screenshots/{name}')
        # os.mkdir(f'screenshots/{name}/{self.start}')
        errorElem = self.checkLink(anchorTags=self.anchorTags, currentUrl=self.url)
        if(errorElem):
            
            href = errorElem.get('href')
            self.driver.get(self.url)
            self.driver.execute_script(f'''document.querySelectorAll("a[href='{href}']")[0].style.border="5px solid red"''')
            filename =str(datetime.now().timestamp())
            # print(f'screenshots/{self.start}/{self.name}/{filename}logError.png')
            if(not os.path.exists(f'screenshots/{name}/{self.start}')):
                os.mkdir(f'screenshots/{name}/{self.start}')
            self.driver.save_screenshot(f'screenshots/{name}/{self.start}/{filename}.png')
        print("Visited ",self.visited)
        self.driver.quit()





# print(visited)
# print(len(visited))

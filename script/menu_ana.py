from bs4 import BeautifulSoup
from utils import getCurClassPage
from download import getBlogPage

class SinaMenuAna:
    def __init__(self, beginPage, cookies, header):
        self.curPage = beginPage
        self.cookies = cookies
        self.header =  header
        self.articleList = []
    
    def getAllArticlePage(self):
        self.handle()
        return self.articleList


    def handle(self):
        # 解析HTML
        pageContent = getBlogPage(self.curPage, self.cookies, self.header)
        soup = BeautifulSoup(pageContent, 'html.parser')  # 注意这里使用了 response.text
        
        article_blk = soup.find('div', {'class': 'articleList'})

        atcInfoList = article_blk.find_all("span",{"class":"atc_title"})
        
        for one in atcInfoList:
            atcUrl = one.find("a",{"target":"_blank"}).get_attribute_list("href")[0]
            self.articleList.append(atcUrl)
        
        nextPageBlk = soup.find("div",{"class":"SG_page"}).find("li",{"class":"SG_pgnext"})
        if nextPageBlk is None:
            return
        nextPage = nextPageBlk.find("a").attrs["href"]
        self.curPage = "https:{}".format(nextPage)
        self.handle()
        


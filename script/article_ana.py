from bs4 import BeautifulSoup

class SinaArticleAna:
    def __init__(self, pageContent):
        self.pageContent = pageContent
    
    def handle(self):
        self.simplify()


    def simplify(self):
                # 解析HTML
        soup = BeautifulSoup(self.pageContent, 'html.parser')  # 注意这里使用了 response.text
        
        # 找到文章内容所在的 <div id="articlebody">
        self.article_body = soup.find('div', {'id': 'articlebody'})
        self.real_article_body =  soup.find("div", {'id': 'sina_keyword_ad_area2'})
        titlePart = soup.find("div",{'class': 'articalTitle'})
        self.title = titlePart.find("h2",{'class': 'titName'}).getText()
        self.time = titlePart.find("span",{'class': 'time'}).getText()
        self.hasImg = (titlePart.find("span",{"class":"img2"}) != None)


    def convMd(self):
        pass

    def write2file(self):
        with open(self.article_name, "w+") as fd:
            pass    

    def downloadImg(self):
        pass

        
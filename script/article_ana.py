from bs4 import BeautifulSoup
from utils import getCurClassPage

article_template = '''
<h2>{title}</h2>

<span class="time SG_txtc">时间: {time} | 分类: [{blogClass}]({classUrl}) | 标签: {tags}</span>
<!--
<table>
    <tbody>
        <tr>
            <td>时间: {time}</td>
            <td>分类: [{blogClass}]({classUrl}) </td>
            <td> 标签: {tags} </td>
        </tr>
    </tbody>
</table>
-->
{content}
'''

class SinaArticleAna:
    def __init__(self, pageContent):
        self.pageContent = pageContent
    
    def handle(self):
        self.simplify()
        self.convMd()
        self.downloadImg()
        self.write2file()


    def simplify(self):
        # 解析HTML
        soup = BeautifulSoup(self.pageContent, 'html.parser')  # 注意这里使用了 response.text
        
        # 找到文章内容所在的 <div id="articlebody">
        self.article_body = soup.find('div', {'id': 'articlebody'})

        # 正文部分
        self.body_str =  str(soup.find("div", {'id': 'sina_keyword_ad_area2'}))
   
        titlePart = soup.find("div",{'class': 'articalTitle'})

        # 标题
        self.title = str(titlePart.find("h2",{'class': 'titName'}).getText())

        # 具体时间、日期
        self.time = titlePart.find("span",{'class': 'time'}).getText()[1:-1]
        self.date = self.time.split(" ")[0]

        # 正文是否包含图片需要下载
        self.hasImg = (titlePart.find("span",{"class":"img2"}) != None)

        tagPart = soup.find("div",{"class":"articalTag"})

        # 标签
        blogTag = tagPart.find("td",{"class":"blog_tag"})
        self.blogTags = [one.getText() for one in blogTag.find_all("h3")]

        # 分类
        self.blogClass = tagPart.find("td",{"class":"blog_class"}).find("a").getText()

    def convMd(self):
        self.content = article_template.format(title=self.title,time=self.time,blogClass=self.blogClass, tags= ",".join(self.blogTags),content=self.body_str,classUrl = getCurClassPage(self.blogClass))

    def write2file(self):
        with open("./articles/{}_{}.md".format(self.date, self.title), "w+") as fd:
            fd.write(self.content)
        print("write to md done.")

    def downloadImg(self):
        if self.hasImg:
            # TODO
            print("has img")

    def getClassInfo(self):
        return self.blogClass, "{}_{}".format(self.date, self.title)
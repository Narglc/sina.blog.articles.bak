from bs4 import BeautifulSoup
from utils import getCurClassPage
from download import getBlogPage, downloadImg, getImgReqHeader

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
    def __init__(self, atcUrl, cookies,header):
        self.articleUrl = atcUrl
        self.cookies = cookies
        self.header = header
        self.hasImg = False
        self.isAvaiable = False
    
    def handle(self):
        self.getAtcPage()
        self.simplify()
        self.downloadImg()
        self.convMd()
        self.write2file()

    def getAtcPage(self):
        pageContent = getBlogPage(self.articleUrl, self.cookies, self.header)
        if pageContent:
            self.pageContent = pageContent
            self.isAvaiable = True

    def simplify(self):
        if self.isAvaiable is False:
            return

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

        # 分类: 有些文章会有多个分类？ 只选取第一个分类？
        blogClassBlk = tagPart.find("td",{"class":"blog_class"}).find("a")
        if blogClassBlk is None: 
            self.blogClass = "未分类博文"
        else:
            self.blogClass = blogClassBlk.getText()

    def convMd(self):
        if self.isAvaiable is False:
            return
        self.content = article_template.format(title=self.title,time=self.time,blogClass=self.blogClass, tags= ",".join(self.blogTags),content=self.body_str,classUrl = getCurClassPage(self.blogClass))

    def write2file(self):
        if self.isAvaiable is False:
            return
        with open("./articles/{}_{}.md".format(self.date, self.title), "w+") as fd:
            fd.write(self.content)
        print("write {}_{} to md done.".format(self.date, self.title))

    def downloadImg(self):
        if self.hasImg:
            soup = BeautifulSoup(self.body_str, 'html.parser')
            allImgs = soup.find_all("img")
            for imgBlk in allImgs:
                alt = imgBlk.attrs["alt"]
                src = imgBlk.attrs["real_src"]
                title = imgBlk.attrs["title"]
                imgOriName = src.split("/")[-1]  
                picName = "{}_{}".format(title, imgOriName)
                localSavePicPath = "./articles/pic/{}".format(picName)                 
                postfix, ok  = downloadImg(src,getImgReqHeader(imgOriName), localSavePicPath)
                print("downloadImg {},oriName:{},alt:{},title:{},src:{},".format("succ" if ok else"fail", imgOriName,alt,title,src))
                if ok:
                    # 创建新的img标签
                    localPicPathInMd = "./pic/{}{}".format(picName, postfix)
                    new_img_tag = soup.new_tag('img', src=localPicPathInMd, alt=alt, title=title)
                    # 将要替换的段落标签替换为新的段落标签
                    imgBlk.replace_with(new_img_tag)
            # 更新原始的 HTML 字符串
            self.body_str = str(soup)

    def getClassInfo(self):
        if self.isAvaiable is False:
            return "",""
        return self.blogClass, "{}_{}".format(self.date, self.title)
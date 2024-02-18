from article_ana import SinaArticleAna
from catalog_summary import SinaCatalogSummary
from download import get_article_content,getCookies,getHeader
# from urllib.parse import unquote

# # 测试代码
if __name__ == "__main__":
    cataSummary = SinaCatalogSummary()

    # 替换为你要爬取的新浪博客文章链接
    article_url = "https://blog.sina.com.cn/s/blog_497675f20100an52.html"

    pageHtml = get_article_content(article_url, getCookies(), getHeader())
    
    if pageHtml: 
        # 处理文章
        articleAna = SinaArticleAna(pageHtml)
        articleAna.handle()
        bClass, bTitle = articleAna.getClassInfo()
        cataSummary.append(bClass,bTitle)
        print("got here...")

    # 生成分类页面
    cataSummary.summary()
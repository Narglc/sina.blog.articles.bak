from article_ana import SinaArticleAna
from menu_ana import SinaMenuAna
from catalog_summary import SinaCatalogSummary
from download import getCookies,getHeader
import time
# from urllib.parse import unquote

# # 测试代码
if __name__ == "__main__":
    cataSummary = SinaCatalogSummary()

    # 博文目录下的“全部博文”页面
    public_blogs = "https://blog.sina.com.cn/s/articlelist_1232500210_0_1.html"

    # 博文目录下的“秘密博文”页面
    private_blogs = "https://control.blog.sina.com.cn/blog_rebuild/blog/controllers/articlelist.php?uid=1232500210&p=1&status=5"

    all_kinds_blogs = [public_blogs, private_blogs]
    cookies = getCookies()
    header = getHeader()

    # 所有文章URL列表
    articlePageList = ["//blog.sina.com.cn/s/blog_497675f2010009qe.html"]

    for beginPage in all_kinds_blogs:        
        menuAna = SinaMenuAna(beginPage, cookies, header)
        cur_menu = menuAna.getAllArticlePage()
        articlePageList.extend(cur_menu)

    # 记录失败的文章列表
    failArticleUrls = []

    for oneUrl in articlePageList:
        try:
            # 处理文章
            articleUrl = "https:{}".format(oneUrl)
            articleAna = SinaArticleAna(articleUrl, cookies, header)
            articleAna.handle()
            bClass, bTitle = articleAna.getClassInfo()
            if bClass != "":
                cataSummary.append(bClass,bTitle)
        except Exception as e:
            print("ArticleAna:{} fail, err:{}".format(oneUrl, e))
            failArticleUrls = failArticleUrls.append(oneUrl)
        # 减小风控
        time.sleep(5)



    # 生成分类页面
    cataSummary.summary()
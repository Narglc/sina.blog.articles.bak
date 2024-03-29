from article_ana import SinaArticleAna
from menu_ana import SinaMenuAna
from catalog_summary import SinaCatalogSummary
from download import getCookies,getHeader
from utils import readYamlConfig
import time
from dao import SQLiteManager

def spiderArticleList(articlePageList, db_mgr):
    # 记录失败的文章列表
    failArticleUrls = []
    for oneUrl in articlePageList:
        try:
            # 处理文章
            articleUrl = "https:{}".format(oneUrl)
            article_id = oneUrl.split('/')[-1].split('_')[-1].split('.')[0]
            
            # 已经拉群的文章跳过
            if db_mgr.checkArticleExist(article_id):
                continue
            articleAna = SinaArticleAna(articleUrl, article_id, cookies, header, db_mgr)
            articleAna.handle()
        except Exception as e:
            print("ArticleAna:{} fail, err:{}".format(oneUrl, e))
            failArticleUrls.append(oneUrl)
        # 减小风控
        time.sleep(3)
    
    return failArticleUrls

# # 测试代码
if __name__ == "__main__":
    # 读取 YAML 配置文件
    config = readYamlConfig('./script/config/config.yaml')

    public_blogs = config["blogs"]["public_blogs_menu"]
    private_blogs = config["blogs"]["private_blogs_menu"]

    all_kinds_blogs = [public_blogs, private_blogs]

    cookies_str = config["blogs"]["cookies_str"]
    cookies = getCookies(cookies_str)
    header = getHeader()

    dbfile = config["db"]["fileName"]
    db_mgr = SQLiteManager(dbfile)
    

    # 获取所有文章URL列表
    articlePageList = []
    for beginPage in all_kinds_blogs:
        if beginPage is None or beginPage == "":
            continue
        menuAna = SinaMenuAna(beginPage, cookies, header)
        cur_menu = menuAna.getAllArticlePage()
        articlePageList.extend(cur_menu)

    # 下载文章到本地
    while len(articlePageList) != 0:
        failArticleUrls = spiderArticleList(articlePageList, db_mgr)
        print("spiderArticle fail:{}".format(failArticleUrls))
        articlePageList = failArticleUrls
        time.sleep(5)

    # 生成分类页面及汇总README.md
    cataSummary = SinaCatalogSummary(db_mgr)
    cataSummary.summary()
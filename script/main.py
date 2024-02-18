import requests
from bs4 import BeautifulSoup
from article_ana import SinaArticleAna
from catalog_summary import SinaCatalogSummary
# from urllib.parse import unquote


def get_article_content(url, cookies=None, headers=None):
    # 发送GET请求获取网页内容
    response = requests.get(url, cookies=cookies, headers=headers, timeout=10, verify=True)

    
    # 设置正确的编码方式
    response.encoding = 'utf-8'  # 或者是页面的实际编码方式

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')  # 注意这里使用了 response.text
        
        # 找到文章内容所在的 <div id="articlebody">
        article_body = soup.find('div', {'id': 'articlebody'})
        
        if article_body:
            # 返回文章内容
            return article_body.get_text()
        else:
            print("未找到文章内容！")
            return None
    else:
        print("请求失败！")
        return None


def getCookies():
    cookies = {}
    with open("script/config/cookies.html","r+") as fd:
        cookies_str = fd.read()
        # 将Cookie字符串转换为字典
        cookies_list = cookies_str.split("; ")
        
        for cookie in cookies_list:
            key, value = cookie.split("=")
            cookies[key] = value
    return cookies

# # 测试代码
# if __name__ == "__main__":
#     # 替换为你要爬取的新浪博客文章链接
#     article_url = "https://blog.sina.com.cn/s/blog_497675f20100an52.html"
    
#     # 替换为你的Cookie字典，如果没有Cookie则为None
#     cookies = getCookies()
#     headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate, sdch, br",
#         "Accept-Language": "zh-CN,zh;q=0.8",
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
#         "Host": "blog.sina.com.cn",
#         "Accept":"*/*"
#     }
    
#     article_content = get_article_content(article_url, cookies, headers)
    
#     if article_content:
#         print(article_content)

# 测试
if __name__ == "__main__":
    cataSummary = SinaCatalogSummary()

    with open("articles/origin.html","r+") as fd:
        # 处理文章
        articleAna = SinaArticleAna(fd)
        articleAna.handle()
        bClass, bTitle = articleAna.getClassInfo()
        cataSummary.append(bClass,bTitle)
        print("got here...")

    # 生成分类页面
    cataSummary.summary()
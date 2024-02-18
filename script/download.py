import requests

def get_article_content(url, cookies=None, headers=None):
    # 发送GET请求获取网页内容
    response = requests.get(url, cookies=cookies, headers=headers, timeout=10, verify=True)

    # 设置正确的编码方式
    response.encoding = 'utf-8'  # 或者是页面的实际编码方式

    # 检查请求是否成功
    if response.status_code == 200:
        return response.content
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

def getHeader():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        "Host": "blog.sina.com.cn",
        "Accept":"*/*"
    }
    return headers
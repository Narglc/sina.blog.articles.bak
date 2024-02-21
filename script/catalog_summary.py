
from utils import getCurClassPage

# 改为存储到sqlite3
class SinaCatalogSummary:
    def __init__(self, mgr):
        self.dbMgr = mgr

    def summary(self):
        rdfd = open("./README.md","a+")
        rdfd.write("----\n")

        # 生成分类汇总页面 并汇总 README.md
        alltypes = self.dbMgr.getAllClassTypes()
        for one in alltypes:
            bClassId = one["id"]
            bClass = one["type"]
            with open("./articles/{}".format(getCurClassPage(bClass)), "w+") as fd:
                titleSet = self.dbMgr.getOneTypeArticlesList(bClassId)
                fd.write("## {}\n".format(bClass))
                rdfd.write("## {}\n".format(bClass))
                for article in titleSet:
                    title = "{}_{}".format(article["created_at"].replace(" ","_"),article["title"])
                    fd.write("- [{}](./{}.md)\n".format(title,title))
                    rdfd.write("- [{}](./articles/{}.md)\n".format(title,title))



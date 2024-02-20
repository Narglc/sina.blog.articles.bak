
from utils import getCurClassPage

class SinaCatalogSummary:
    def __init__(self):
        self.blogClassDict = {}

    
    def append(self, bClass, bTitle):
        if bClass not in self.blogClassDict:
            self.blogClassDict[bClass] = set()
            
        self.blogClassDict[bClass].add(bTitle)

    def summary(self):
        rdfd = open("./README.md","a+")
        rdfd.write("----\n")

        # 生成分类汇总页面 并汇总 README.md
        for bClass, titleSet in self.blogClassDict.items():
            with open("./articles/{}".format(getCurClassPage(bClass)), "w+") as fd:
                fd.write("## {}\n".format(bClass))
                rdfd.write("## {}\n".format(bClass))
                # 按时间排序
                titleList = sorted(titleSet)
                for title in titleList:
                    fd.write("- [{}](./{}.md)\n".format(title,title))
                    rdfd.write("- [{}](./articles/{}.md)\n".format(title,title))



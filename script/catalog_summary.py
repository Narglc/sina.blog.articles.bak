
from utils import getCurClassPage

class SinaCatalogSummary:
    def __init__(self):
        self.blogClassDict = {}

    
    def append(self, bClass, bTitle):
        if bClass not in self.blogClassDict:
            self.blogClassDict[bClass] = set()
            
        self.blogClassDict[bClass].add(bTitle)

    def summary(self):
        # 生成分类汇总页面
        for bClass, titleSet in self.blogClassDict.items():
            with open("./articles/{}".format(getCurClassPage(bClass)), "w+") as fd:
                fd.write("## {}\n".format(bClass))
                for title in titleSet:
                    fd.write("- [{}](./{}.md)\n".format(title,title))

        # 重构 README.md
        # TODO
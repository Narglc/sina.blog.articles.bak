import yaml

# 分类页面也使用md
class_page = "./BlogClass_{}.md"

def getCurClassPage(bClass):
    return class_page.format(bClass)


def readYamlConfig(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config
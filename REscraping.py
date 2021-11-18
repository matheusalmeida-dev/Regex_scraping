from urllib.request import urlopen
import re
import json

xml = urlopen("https://www.globo.com/").read()

xmlTitulo = re.compile(r'<h3 class=\"post__title\">(.*?)<\/h3>')
findTitulo = re.findall(xmlTitulo,xml.decode("utf-8"))

with open('noticiasGLOBO.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(findTitulo, indent=4)
    jp.write(js)
# -*- coding: utf-8 -*-
import re
import requests

projectListUrl = "http://www.src.cool/forum.php?mod=forumdisplay&fid=36&filter=&orderby=lastpost&page=%d"

projectList = []
def getOnePage(pageNum):
    response = requests.get(projectListUrl % pageNum)
    #print(response.text)
    pl = re.findall(r'回复: <a href="thread-.*?.html', response.text)
    projectList.extend(pl)
    print(projectList)

# -*- coding: utf-8 -*-
import re
import requests

projectUrl = "http://www.src.cool/%s"

def isHaveKeyWord(projectLink, keyWrod):
    response = requests.get(projectUrl % projectLink)
    #print(response.text)
    resultList = re.findall(keyWrod, response.text)
    if len(resultList) > 0:
        return True

    return False

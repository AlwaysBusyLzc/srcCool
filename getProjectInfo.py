# -*- coding: utf-8 -*-
import re
import requests

projectUrl = "http://www.src.cool/%s"

def isHaveKeyWord(projectLink, keyWrod):
    response = requests.get(projectUrl % projectLink)
    #print(response.text)

    for word in keyWrod:
        resultList = re.findall(word, response.text, re.I)
        if len(resultList) == 0:
            return False

    return True

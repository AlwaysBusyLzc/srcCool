# -*- coding: utf-8 -*-
import time
from multiprocessing.dummy import Pool

import getProjectLink
import getProjectInfo


keyWord = "python"

#print(getProjectInfo.isHaveKeyWord("thread-1365-1-1.html", keyWord))


for i in range(14):
    print("page %d" % i)
    getProjectLink.getOnePage(i)

realNeedUrlList = []


def dealOneProject(project):
    if getProjectInfo.isHaveKeyWord(str(project).split('="')[1], keyWord):
        realNeedUrlList.append(getProjectInfo.projectUrl % str(project).split('="')[1])

for project in getProjectLink.projectList:
    dealOneProject(project)

def parseAll(processes=10):
    """ 并发分析 """
    start_time = time.time()
    pool = Pool(processes)
    for project in getProjectLink.projectList:
        pool.apply_async(dealOneProject, (project, ))

    pool.close()
    pool.join()
    end_time = time.time()
    print('分析完毕,用时:%s秒' % (end_time - start_time))


#parseAll(processes=10)

print(realNeedUrlList)


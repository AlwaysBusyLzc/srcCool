# -*- coding: utf-8 -*-
import time
from multiprocessing import Pool
import getProjectLink
import getProjectInfo

keyWord = "python"


def dealOneProject(project):
    if getProjectInfo.isHaveKeyWord(str(project).split('="')[1], keyWord):
        return getProjectInfo.projectUrl % str(project).split('="')[1]
    return ""


def parseAll(urlSet, processes=10):
    """ 并发分析 """
    start_time = time.time()
    pool = Pool(processes)
    for project in getProjectLink.projectList:
        urlSet.append(pool.apply_async(dealOneProject, args=(project,)))

    pool.close()
    pool.join()

    end_time = time.time()
    print('分析完毕,用时:%s秒' % (end_time - start_time))


if __name__ == '__main__':
    for i in range(14):
        print("page %d" % i)
        getProjectLink.getOnePage(i)

    realNeedUrlSet = []
    parseAll(realNeedUrlSet, processes=10)
    print([x.get() for x in realNeedUrlSet if x.get() != ""])

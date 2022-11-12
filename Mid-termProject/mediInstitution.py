import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

ServiceKey = "rX0WAdrv4MYSvgvMgVKuBiNN1%2BkHA2lDHgbzzvOI%2F95pXZrq%2FlmMj0jt6KCI1NMHGfV0BQTPOsd7kPoAeT7p9Q%3D%3D"


def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def getItem(apiType):
    service_url = "http://apis.data.go.kr/1352000/ODMS_STAT_14/callStat14Api"
    parameters = "?serviceKey=" + ServiceKey  # 인증키
    parameters += "&pageNo=" + "1"
    parameters += "&numOfRows=" + "85"
    parameters += "&apiType=" + apiType
    # parameters += "&year=" + "2015"

    url = service_url + parameters
    retData = getRequestUrl(url)
    # print(retData)

    if (retData == None):
        return None
    else:
        return json.loads(retData)


def getService(apiType):
    jsonResult = []
    result = []
    year = ''
    dvsd = ''
    ttl = ''
    jsonData = getItem(apiType)

    if (jsonData['resultCode'] == '00'):
        if jsonData['items'] == '':
            print("데이터 없음....")

        else:
            print(json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False))
            for i in range(0, 85):
                year = jsonData['items'][i]['year']
                dvsd = jsonData['items'][i]['dvsd']
                totalCount = jsonData['totalCount']
                ttl = jsonData['items'][i]['ttl']
                print('[ %s %s %s ]' % (year, dvsd, ttl))
                print('----------------------------------------------------------------------')
                jsonResult.append({'year': year, 'dvsd': dvsd, 'totalCount': totalCount, 'sum': sum})
                result.append([year, dvsd, ttl])

            return (jsonResult, result, year, dvsd, ttl)


def main():
    jsonResult = []
    result = []
    y15, y16, y17, y18, y19 = [], [], [], [], []
    print(">>>>>>>> 크롤링 시작")
    apiType = "JSON"

    jsonResult, result, year, dvsd, ttl = getService(apiType)

    # 파일 저장
    columns = ["년도", "지역", "병원 수"]
    for y in result:
        if y[0] == '2015':
            y15.append(y)
        elif y[0] == '2016':
            y16.append(y)
        elif y[0] == '2017':
            y17.append(y)
        elif y[0] == '2018':
            y18.append(y)
        elif y[0] == '2019':
            y19.append(y)
    rst = [y15, y16, y17, y18, y19]
    result = pd.DataFrame(result, columns=columns)
    result.to_csv('hospitals.csv', index=False, encoding='utf-8')

    ##그래프 그리기
    import matplotlib.pyplot as plt
    import numpy as np

    def graph1():
        for num, i in enumerate(rst):
            lst = []
            x = np.arange(17)
            for j in i:
                tmp = [j[1], int(j[2])]
                lst.append(tmp)
                lst.sort(key=lambda x: x[1])
            rg, nm = [], []
            for i in lst:
                rg.append(i[0])
                nm.append(i[1])

            plt.bar(x, nm)
            plt.title(str(num + 2015) + "년도 보건의료기관 소재지별 의료기관수 ")
            plt.xticks(x, rg)
            plt.show()

    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False

    graph1()

    def graph2():
        nm = []
        r = [[] for _ in range(17)]
        years = [2015, 2016, 2017, 2018, 2019]
        name = []

        for bf, i in enumerate(rst):
            i.sort(key=lambda x: x[1])
            for num, j in enumerate(i):
                r[num].append(int(j[2]))
                if bf == 0:
                    name.append(j[1])

        for i in range(17):
            plt.plot(years, r[i], "-o", label=name[i])
            plt.xticks(years)
            plt.legend()

        plt.xlabel('년도')
        plt.ylabel('병원 및 의원 수')
        plt.show()

    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False

    graph2()


if __name__ == '__main__':
    main()
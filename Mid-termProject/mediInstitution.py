import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

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


def getItem(apiType, dvsd, year):
    service_url = "http://apis.data.go.kr/1352000/ODMS_STAT_14/callStat14Api"
    parameters = "?serviceKey=" + ServiceKey  # 인증키
    parameters += "&pageNo=" + "1"
    parameters += "&numOfRows=" + "85"
    parameters += "&apiType=" + apiType
    parameters += "&year=" + str(year)
    parameters += "&dvsd=" + dvsd

    url = service_url + parameters

    retData = getRequestUrl(url)
    # print(retData)

    if (retData == None):
        return None
    else:
        return json.loads(retData)


def getService(apiType, dvsd, year, result, mpl):
    # jsonResult = []
    # result = []
    dvsd = ''
    ttl = ''
    jsonData = getItem(apiType, dvsd, year)

    if (jsonData['resultCode'] == '00'):
        if jsonData['items'] == '':
            print("데이터 없음....")

        else:
            print(json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False))
            tmp = []
            for i in range(len(jsonData['items'])):
                year = jsonData['items'][i]['year']
                dvsd = jsonData['items'][i]['dvsd']
                ttl = jsonData['items'][i]['ttl']
                print('[ %s %s %s ]' % (year, dvsd, ttl))
                print('----------------------------------------------------------------------')
                tmp.append([year, dvsd, ttl])
                result.append([year, dvsd, ttl])
            mpl.append(tmp)
        return (result, year, dvsd, ttl, mpl)


def main():
    mpl = []
    result = []
    dvsd = ''
    # y15, y16, y17, y18, y19 = [], [], [], [], []
    print(">>>>>>>> 크롤링 시작")
    apiType = "JSON"
    yr = [2015, 2016, 2017, 2018, 2019]
    for i in yr:
        result, ttl, dvsd, year, mpl = getService(apiType, dvsd, i, result, mpl)
    print(result)
    print(mpl)
    # 파일 저장
    columns = ["년도", "지역", "병원 수"]
    result = pd.DataFrame(result, columns=columns)
    result.to_csv('./hospitals.csv', index=False, encoding='utf-8')

    ##그래프 그리기
    import matplotlib.pyplot as plt
    import numpy as np

    def graph1(mpl):
        for num, i in enumerate(mpl):
            lst, tmp = [], []
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
            plt.title(str(num + 2015) + "년도 보건의료기관 소재지별 의료기관수")
            plt.xticks(x, rg)
            plt.show()

    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False
    graph1(mpl)

    def graph2(mpl):
        nm = []
        r = [[] for _ in range(17)]
        years = [2015, 2016, 2017, 2018, 2019]
        name = []

        for bf, i in enumerate(mpl):
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
        plt.ylabel('의료 기관 수')
        plt.show()

    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False
    graph2(mpl)


if __name__ == '__main__':
    main()
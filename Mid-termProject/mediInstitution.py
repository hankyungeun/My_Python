import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt

ServiceKey = "rX0WAdrv4MYSvgvMgVKuBiNN1%2BkHA2lDHgbzzvOI%2F95pXZrq%2FlmMj0jt6KCI1NMHGfV0BQTPOsd7kPoAeT7p9Q%3D%3D"


# [CODE 1]
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


# [CODE 2]
def getItem(apiType):
    service_url = "http://apis.data.go.kr/1352000/ODMS_STAT_14/callStat14Api"
    parameters = "?serviceKey=" + ServiceKey  # 인증키
    parameters += "&pageNo=" + "1"
    parameters += "&numOfRows=" + "85"
    parameters += "&apiType=" + apiType
    # parameters += "&year=" + "2015"

    url = service_url + parameters

    retData = getRequestUrl(url)  # [CODE 1]

    # print(retData)

    if (retData == None):
        return None
    else:
        return json.loads(retData)


# [CODE 3]
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
            for i in range(0,85):
                year = jsonData['items'][i]['year']
                dvsd = jsonData['items'][i]['dvsd']
                totalCount = jsonData['totalCount']
                ttl = jsonData['items'][i]['ttl']
                print('[ %s %s %s ]' % (year, dvsd, ttl))
                print('----------------------------------------------------------------------')
                jsonResult.append({'year': year, 'dvsd': dvsd,'totalCount': totalCount, 'sum': sum})
                result.append([year, dvsd, ttl])

            return (jsonResult, result, year, dvsd, ttl)


def main():
    jsonResult = []
    result = []
    print(">>>>>>>> 크롤링 시작")
    apiType = "JSON"


    jsonResult, result, year, dvsd, ttl = getService(apiType)


    #파일 저장
    columns = ["년도", "지역", "병원 수"]
    result = pd.DataFrame(result, columns=columns)
    result.to_csv('hospitals.csv', index=False, encoding='utf-8')



    ##그래프 그리기
    import matplotlib
    from matplotlib import font_manager, rc

    # 1) 그래프의 Y축 데이터 : 방문객 수 visitCnt[]
    # 2) 그래프의 X축 데이터 : 방문 년월 visitYM[]
    visitCnt = []
    visitYM = []
    index = []
    i = 0
    for item in jsonResult:
        index.append(i)
        visitCnt.append(item['dvsd'])
        visitYM.append(item['year'])
        i += 1

    # font_path = "/Users/hangyeong-eun/Documents/My_Python/malgun.ttf"
    # font = font_manager.FontProperties(fname=font_path).get_name()
    # matplotlib.rc('font', family=font)

    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False



    plt.xticks(index, visitYM)
    plt.plot(index, visitCnt)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd 


def step1_GetData():
    print('step1_GetData is working...')
    ### 영화코드
    code_list = [204624, 191597]
    # 현재 크롤링 중인 영화가 첫번째 영화인지 여부
    chk = False

    ## 영화 개수 만큼 반복
    for code in code_list:
        
        # 1단계 : 해당 영화의 평점 페이지 수 계산
        site1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=%d&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'% code
        print(site1)
        res1 = requests.get(site1)
        if res1.status_code == requests.codes.ok: ## 페킷이 잘 넘어왔는지 확인. 주로 만날 번호는 400번대와 200, 500번대. 를 확인하는 명령어
            ## 접속 잘되면, 200대,  ok
            ## 접속 잘안되면, 404
            ## 500번대는 요청한 url은 있는데, 로직이 에러났을 경우. 
            ## 정상 ok이면 이제 html 코드 분석 실시
            bs1 = BeautifulSoup(res1.text, 'html.parser')
            


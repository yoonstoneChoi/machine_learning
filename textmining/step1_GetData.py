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
        res1 = requests.get(site1)
        if res1.status_code == requests.codes.ok: ## 페킷이 잘 넘어왔는지 확인. 주로 만날 번호는 400번대와 200, 500번대. 를 확인하는 명령어
            # print(res1.status_code)
            ## 접속 잘되면, 200대,  ok
            ## 접속 잘안되면, 404
            ## 500번대는 요청한 url은 있는데, 로직이 에러났을 경우. 
            ## 정상 ok이면 이제 html 코드 분석 실시
    
  

            #html 코드 분석
            bs1 = BeautifulSoup(res1.text, 'html.parser')

            score_total = bs1.find(class_ = 'score_total')
            ems = score_total.find_all('em')
            score_total = int(ems[0].text.replace(',',''))

            ## 페이지 수 계산 
            pageCnt = score_total // 10
            if score_total % 10 > 0:
                pageCnt += 1
            print('전체 페이지 수 :',pageCnt)

            # 현재 루프돌고 있는 페이지 번호 표시
            now_page = 1
            # pageCnt = 2 ## 잠시 테스트를 위한 초기화

            # 평점 글, 평점 등 필요한 정보 가져오기 
            while now_page <= pageCnt:
                sleep(0.5)
                site2 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=%d&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=%d'% (code, now_page)
                res2 = requests.get(site2)
                if res2.status_code == requests.codes.ko:
                    bs2 = BeautifulSoup(res2, 'html-parser')
                    score_result = bs2.find(class_='score_result')
                    lis = score_result.find_all('li')
                    df = pd.DataFrame()
                    for obj in lis:
                        # 평점
                        star_score = obj.find(class_ = 'star_score')
                        star_em = star_score.find('em')
                        star_score = int(star_em.text)
                        # 평가글
                        score_reple = obj.find(class_ = 'score_reple')
                        reple_ptag = score_reple.find('p')
                        reple_ptag_span = reple_ptag.find_all('span')
                        #score_reple = reple_ptag_span[1].text
                        # ID
                        reple_id = obj.find(class_ = 'score_reple')
                        id_a = reple_id.find('a')

                        id_span = reple_id.find_all('span')
                        id = id_span[2].text

                        # 데이터 누적
                        df = df.append([id, score_reple, star_score], ignore_index=True)
            
                    # 저장 : 처음 저장(파일이 없을때), 두번째 이후 저장(파일이 있을때)
                    if chk == False:
                        df.columns = ['id', 'text', 'star']
                        df.to_csv('naver_star_data.csv', index = False, encoding= 'utf-8')
                    else:
                        df.to_csv('naver_star_data.csv', index =False, encoding = 'utf-8', mode = 'a', header = False)

                print('%d / %d' % (now_page, pageCnt))
                now_page += 1
 




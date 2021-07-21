import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split



def star_preprocessing():
    print('star_preprocessing is now working...')
    value = int(text)
    if value <= 5:
        return 0
    else:
        return 1
    print('star_preprocessing done')



def step2_Preprocessing():
    print('step_2 is now working2....')
    ## 수집 데이터 읽어오기
    df = pd.read_csv('naver_star_data.csv')
    # print(df.header())
    # train-test-split 을 이용하지 못한 경우 -> 데이터터를 랜덤하게 섞어줘야 한다. 
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))


    # 전처리
    # text 컬럼 내용을 정리 -> 지금은 할게 없음
    # 평점 데이터를 레이블 작업 -> 평점 5점 이상이면 1, 아니면 0
    df['star'] = df['star'].apply(star_preprocessing)
    
    text_list = df['text'].tolist()
    star_list = df['star'].tolist()

    text_train, text_test, star_train, star_test = train_test_split(text_list, star_list, test_size = 0.2, random_state = 0)
    print(len(text_train), len(star_train),len(text_test) ,len(star_test))

    ## 저장을 위한 데이터 프레임 작업
    dic_train = {'text' : text_train, 'star' : star_train}
    df_tran = pd.DataFrame(dic_train)
    dic_test = {'text' : text_test, 'star' : star_test}
    df_test = pd.DataFrame(dic_test)

    ## 저장
    df_tran.to_csv('naver_train_data.csv', index = False, encoding='utf-8')
    df_test.to_csv('naver_test_data.csv', index = False, encoding='utf-8')

    print('step_2 done')




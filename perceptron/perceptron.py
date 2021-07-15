import numpy as np 

class Perceptron:
    ## 생성자
    ## 초기값, default값 생성
    ## thresholds : 임계값, 계싼된 예측값을 비교하는 값
    ## eta : 학습률
    ## n_iter : 학습횟수
    def __init__(self, thresholds = 0.0 , eta =0.01, n_iter = 10): ## 생성자 매써드
        self.threshold = thresholds
        self.eta = eta
        self.n_iter = n_iter

    ## 학습 
    def fit(self, X, y):
        pass
        

    ## 가중치(w) * 입력값(X) 총합 계산, 매트릭스 계산
    # X : 입력값      
    def net_input(self, X):
        ## 각 자리의 값과 가중치를 곱한 총합
        a1 = np.dot(X, self.w_[1:]) + self.w_[0]
        return a1
    
    ## 예측된 결과를 가지고 판단
    ## X : 입력값, 배열
    def predict(self, X):
        a2 = np.where(self.net_input(X) > self.threshold,1, -1)
        return a2


    

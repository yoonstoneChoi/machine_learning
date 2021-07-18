import numpy as np 

class PerceptronPra:
    def __init__(self, thresholds = 0.0, eta = 0, n_iter = 10):
        ## 생성자
        ## 초기값 default값 생성
        ## thresholds = 임계값, 계산된 예측값을 비교하는 값
        ## eta = 학습률, learning rate, alph
        ## n_iter = 학습률
        self.thresholds = thresholds
        self.eta = eta
        self.n_iter= n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1]) ## w백터와 바이어스 생성

        ## 예측값과 실제값을 비교해서, 다른 예측 값의 개수를 담을 리스트 
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0 ## 초기화겠지? 

            ## 임시변수 생성: 입력받은 입력값과 결과값을 묶는다. 
            temp1 = zip(X,y)
            



# 네이버 영화 텍스트 마이닝


## url 분석을 가장 먼저 해야 함(url의 변화를 잘 확인해야 함)
## 링크를 컨트롤 키를 누르고 선택하면, 새탭으로 창이떠서, url 정보를 확인하기 용이하다. 

## ?를 기준으로 쿼리 스트링이 나옴(서버에 요청을 주기 위한 get 방식, 키벨류 형태고( =을 통해 키 밸류 구분), 구분자는 &(엔퍼센트)를 사용)

 
## 예시 링크 
## https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=191597&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=2



## 겟방식과 포스트 방식의 차이
## 서버(aPI서버, 왓스, 디비 서버등)와 클라이언트로 나뉜다.
## 클라이언트는 클라이언트 프로그램 : 웹서비스를 이용하는 프로그램 (예를들면 브라우저)
##  웹 소캣을 사용함 클라이언트가 이용하려면. 
## 서버와 클라이언트 간 소통하려면 서로 약속(코드)가 필요함
## 웹에서는, GET과 POST 방식이 그 서로간 약속이다.(그 외에 patch 나 delet 등이 있다)
## 네트웍상 약속을 패킷이라고 한다(0~5byte는 해드, 몇몇~은 바디, 등등의 약속)
## 패킷은 주로 해더와 바디, 해(패)리티비트?(0,1로 나뉜 방식) 로 나뉘어진다.
## 패리티비트는 01로 이뤄져서, 다 더해서 1이 나왔다 하면, 작동 하는 식으로의 고전적 방식. 
## 중간에 데이터가 유실되어있는지 확인 할 수 있다. 1로 보내졌는데 확인해보니 0이었다던지 하는 식으로 확인해서
## get은 header부분을 간소화시키기 위해서, header로 받아야 하는 부분을 쿼리 스트링으로 요청해서 받아옴. 
## ? 뒷 부분을 키밸류 방식으로해서 가져옴. 
## POST방식은 get 방식으로 받기 어려운 느낌.
## post로 보내면, 해더안에 매새지라는 영역에 실제 메세지를 넣어서 처리. url상에 안보이고, 패킷 상에서 post인지 delet인지 등에 데이터들이 들어감
## 극명한 차이는  get은 url안에 쿼리 스트링이 노출되고 post 방식은 url 상에 없고 패킷 안에 정의된다. (양이 많고 안정적인 전송을 위해 post사용)
## 간단한 방식은 get 방식을 사용한다. 
## 주로 크롤링을 할 때에는, 쿼리스트링을 본다. 
## query String parameter를 통해 확인 가능: get 방식
## 서버도 잘 받았어라고 보여주는게, response header(개발자 모드에서 확인 가능)




from step1_GetData import step1_GetData



step1_GetData()

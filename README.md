# deeplearning

회귀분석(Regression Analysis)
선형회귀(Linear Regression) : 독립변수 x를 사용해 종속변수 y의 움직임을 예측하고 설명하는 작업
다중 선형회귀(Multiple Linear Regression) : 다양한 독립변수 x1, x2, x3를 사용해 종속변수 y의 움직임을 예측하고 설명하는 작업
로지스틱 회귀(Logistic Regression) : 독립변수 x를 사용해 종속변수 y의 참, 거짓(성공,실패)을 예측하고 설명하는 작업
 -참과 거짓중에 하나를 출력

    최소 제곱법(Least Squares Method) : 예측 직선을 구할 수 있다
        a(기울기)) = (x - x평균)(y - y평균)의 합 / (x - x평균)제곱의 합 
        b(y의 절편)) = y의 평균 - (x의 평균 * 기울기 a)

        평균 제곱 오차(Mean Squared Error, RSE)
        평균 제곱근 오차(Root Mean Squared Error, RMSE)
         -대용량 데이터이며 RSE 계산속도가 느릴때
        
    오차를 줄이는 방법
         - 경사 하강법(Gradient descent)
           미분(Derivative)을 사용
             -순간변화율, 기울기-방향성이 있다.
             -기울기 a를 변화시켜서 기울기가 0인 m값을 찾아내는 방법
             
             -학습률(learning rate)
              -기울기를 변화시킬 시 잘못된 값이 들어가면 치솟아 버리거나 느려짐
              -학습률은 이동거리를 정해주는것
              -케라스는 자동으로 조절
    
경사 하강법(Gradient descent)
    1. 확률적 경사 하강법(SGD) : 랜덤하게 추출한 일부 데이터를 사용해 더 빨리 자주 업데이트 하게 하는것  
    2. 모멘텀(Momen6tum)
    3. 네스테로프 모멘텀(NAG)
    4. 아다그라드(Adagrad)
    5. 알엠에스프롭(RMSProp)

로지스틱 회귀(Logistic Regression)
 -참과 거짓중에 하나를 출력 해야함
 -합격, 불합격과 같은 명제들 해결
 -그래프를 그려보면 1과 0 사이의 S자 곡선이 나온다
 
 시그모이드(Sigmoid) 함수
  -a가 작아질수록 오차는 무한대로 커짐
  -a가 커진다고 해서 오차가 무한대로 커지지는 않음
  오차공식
   - 경사하강법으로 구함
   - 실제값이 1일 때 예측 값이 0에 가까워지면 오차는 커져야 함
   - 실제값이 0일 때 예측 값이 1에 가까워지면 오차는 커여야 함
   - 로그함수 등장
   - 오차 = -평균(y * logh + (1-y)log(1-h))
   - loss = 오차의 평균값 중 최소값을 찾아가는 과정
  
  퍼셉트론(perceptron)
  -1957년 코넬 항공 연구소 프랑크 로젠블라크가 고안
  -인공신경망의 한 종류, 모델
  -로지스틱 회귀 알고리즘을 이용하여 구현가능

  인공신경망
  다층 퍼셉트론을 이용하여 XOR문제 해결
  다층 퍼셉트론에서 오차를 줄이는 것 --> 이는 경사하강법의 확장개념인 오차역전파로 최적화함

  인간의 뇌
   - 1000억 개의 뉴런으로 이루어져 있음
   - 뉴런과 뉴런 사이에는 시냅스라는 연결 부위가 있음
   - 신경말단에서 자극을 받으면 시냅스에서 화학 물질이 나와 전위변화를 일으킴
   - 전위가 임계값을 넘으면 다음 뉴런으로 신호전달
   - 전위가 임계값을 넘지 못하면 아무일도 일어나지 않음
   - 뉴런의 동작 메카니즘이 로지스틱 회귀와 닮아있음을 착안
   - 뉴런과 비슷한 매커니즘을 인공적으로 사용하면 생각을 만들 수 있지 않을까? - 아이디어
   - 인공 신경망(Arificial Neural Network)
   - 뉴런 -> 신경망 -> 지능
   - 퍼셉트론 -> 인공 신경망 -> 인공지능 가능!! 예상 but, 1969 마빈민스키(Marvin Minsky)

심층신경망(Deep Neural Network, DNN)

------------------------------
빅데이터 분석 솔루션
 - R
 - SAS
 - 에스터



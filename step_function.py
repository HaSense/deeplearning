'''
신경망에서의 활성화 함수는 임계값을 경계로 출력이 바뀝니다.

이런 함수를 계단함수(STEP Function)이라고 합니다.

퍼셉트론에서는 활성화 함수로 계단함수를 이용합니다.
'''
import numpy as np

def intuitive_setp_function(x):
    if x>0 :
        return 1
    else :
        return 0

def step_function(x):
    y = x > 0
    return y.astype(np.int)

#setep function test
x = np.array([-1.0, 1.0, 2.0])
print(x)
y = x > 0
print(y)
y = y.astype(np.int)
print(y)

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

#논리게이트 테스트
print(f'AND(0,0) : {AND(0,0)}')
print(f'AND(0,1) : {AND(0,1)}')
print(f'AND(1,0) : {AND(1,0)}')
print(f'AND(1,1) : {AND(1,1)}')

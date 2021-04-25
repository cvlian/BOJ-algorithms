"""
    Continuous Sum

    Note: 연속합을 구하는 문제
"""

# 연속합이 'k' 가 되는 구간의 개수_2015
# 이전단계까지의 sum을 담고, 현재까지의 합(a[0]+a[1]+ ... + a[i])이 's'라면 딕셔너리 내에 'k-s'의 개수만큼 리턴값에 더해줌.
def make_K(n, k, a):
    D = {0:1} # a[0] = k 인 경우를 대비해 '0'을 미리 딕셔너리에 추가
    s = 0; ret = 0

    for v in a :
        s += v

        if s-k in D:
            ret += D[s-k]
        
        D[s] = 1 if s not in D else D[s] + 1

    return ret
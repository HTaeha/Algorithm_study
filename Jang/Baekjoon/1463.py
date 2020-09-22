memory = [0] * 1000001

def bottom_up(N) :
    memo = [0] * 1000001
    memo[2] = 1
    memo[3] = 1
    for i in range(4, N+1) :
        if i % 2 == 0 and i % 3 != 0 :
            memo[i] = min(memo[i-1], memo[int(i/2)]) + 1
        elif i % 3 == 0 and i % 2 != 0 :
            memo[i] = min(memo[i-1], memo[int(i/3)]) + 1
        elif i % 3 != 0 and i % 2 != 0 :
            memo[i] = memo[i-1] + 1
        else :
            memo[i] = min(memo[i-1], memo[int(i/2)], memo[int(i/3)]) + 1
    return memo[N]

def top_down(N) :
    ret = 10000000
    if memory[N] :
        return memory[N]

    if N == 1 :
        return 0

    if N % 2 == 0 :
        temp = top_down(int(N/2)) + 1
        if temp < ret :
            ret = temp

    if N % 3 == 0 :
        temp = top_down(int(N/3)) + 1
        if temp < ret :
            ret = temp

    temp = top_down(N-1) + 1

    if temp < ret :
        ret = temp

    memory[N] = ret
    return ret

if __name__ == "__main__" :
    N = int(input())
    print(bottom_up(N))
    print(top_down(N))

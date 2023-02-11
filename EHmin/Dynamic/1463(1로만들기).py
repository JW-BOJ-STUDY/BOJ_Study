N = int(input())

dp = [0]* (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
        
print(dp[N]) #1을 계산하는 방식, 4를 계산 하는 방식은 2*2 와 3+1이 있으니, 이렇게 계산해 가는 과정을 기억했다가
#유리한걸 사용해나가겠다
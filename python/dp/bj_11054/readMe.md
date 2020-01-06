## 11054번 
## 가장 긴 바이토닉 부분 수열 

## [문제](https://acmicpc.net/problem/11054)

## 접근법 

* dp[i] = [maximum increasing from left, maximum decreasing to right]
    * dp[i][0] : 왼쪽에서부터 i까지 증가하는 부분수열 중 가장 긴 길이
    * dp[i][1] : i부터 오른쪽끝까지 감소하는 부분수열 중 가장 긴 길이

* 우리가 원하는 것은 sum(dp[n-1])-1 

* dp의 실질부인 2중 for문은 다음과 같다.

```python
for i in range(0, n-1):
    for j in range(i+1, n):
        if src[i] < src[j]:
            dp[j][0] = max(dp[j][0],dp[i][0]+1)
        if src[n-1-i] < src[n-1-j]:
            dp[n-1-j][1] = max(dp[n-1-j][1], dp[n-1-i][1] + 1)
```


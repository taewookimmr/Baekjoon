## 백준 9465번 스티커

## [문제](https://www.acmicpc.net/problem/9465)

## 접근법

dp[x] = [a, b, c]

    * x-th column, bottom row 까지 진행(스티커 때기)했을 때 나올 수 있는 세 가지 경우에서 각각의 최대값을 저장
    * a는 x-th column이 위에서 아래로 0,0일 때의 최대값, (0은 스티커를 안 땜, 1은 땜)
    * b는 ~~ 0,1일 때의 최대값
    * c는 ~~ 1,0일 때의 최대값
    * 이런식으로 dp[x]를 구성했으니 dp[x]로부터 dp[x+1]을 구할 수 있다.
    * 다음의 for문 body를 보면 바로 감이 올 것이다.

```python
for c in range(1, m):
    dp[c][0] = max(dp[c-1])
    dp[c][1] = max(dp[c-1][0], dp[c-1][2]) + stickers[1][c]
    dp[c][2] = max(dp[c-1][0], dp[c-1][1]) + stickers[0][c]
```
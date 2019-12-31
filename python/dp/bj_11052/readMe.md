## 11052번 
## 카드 구매하기

## [문제](https://acmicpc.net/problem/11052)

## 접근법 

* dp 리스트를 만들어 memoization을 이용한다.
    dp[x] : 구입해야할 카드가 x장 남았을 때, 그때까지 지불한 금액(의 최대값) 
    위와 같이 define했으니 dp[0]을 구하는 것이 목적이다.
    ```python
    def solution_simple():
        dp = [0]*(int(input())+1) 
        packs = list(map(int, input().rstrip().split()))
        for i in range(n, -1, -1):
            for j, p in enumerate(packs):
                if i-(j+1) >= 0:
                    dp[i-(j+1)] = max(dp[i-(j+1)], dp[i] + p)           
        print(int(dp[0]))
    ```
* dp[i]인 상태에서, 한 팩에 j+1개의 카드가 들어간 팩을 구매하게 된다면, 앞으로 구매해야할 카드의 개수는 i-(j+1)인 상태가 되고, 그때의 누적 지출액은 dp[i]+p가 된다. 그런데 dp[i-(j+1)]은 조합 가능한 모든 상황에서 나올 수 있는 최대값을 저장해야 하므로 max함수를 사용한다.


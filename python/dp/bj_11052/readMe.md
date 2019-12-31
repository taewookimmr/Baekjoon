## 11052번 
## 카드 구매하기

## [문제](https://acmicpc.net/problem/11052)

## 접근법 

* 비교 해야할 수치의 단위는 [가격/장수]
* 카드 한 장당 가격을 비교해야 한다.
    ```python
    unitPrices = [[e/i,i] for i, e in enumerate(packs) if i]
    # 여기서 e는 i개의 카드가 들어있는 pack의 가격, e/i는 카드 한장당 가격
    unitPrices.sort(reverse=True)
    # 내림차순으로 정렬할 필요는 없었네, 전체적인 코드 동작을 보니
    ```

* dp 리스트를 만들어 memoization을 이용한다.
    dp[x] : 구입해야할 카드가 x장 남았을 때, 그때까지 지불한 금액(의 최대값) 
    위와 같이 define했으니 dp[0]을 구하는 것이 목적이다.
    ```python
    for i in range(n, -1, -1):
            for up, j in unitPrices:
                if i-j >= 0:
                    dp[i-j] = max(dp[i-j], dp[i] + up*j)     
    ```
    * 최외각 for는 dp[n], dp[n-1], 내려가는 방향으로 확인하겠다는 것
    * d[i]인 상태에서 개당 가격이 up인 카드팩(j개의 카드로 구성)을 구매하려고 할 때 다음과 같은 비교를 한다. max함수가 그 비교를 담당한다.
    * d[i-j]의 기존값보다 dp[i]+up*j가 큰 경우에만 갱신하겠다는 것이다.


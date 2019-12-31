## Problem Definition
정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 반환하는 프로그램을 작성하여라

## Detail
when n = 4

1/1/1/1
1/1/2
1/2/1
2/1/1
2/2
1/3
3/1

즉, 순서가 다른 것도 하나로 친다.

## Approach
* dp[x]와 dp[x-1], dp[x-2], dp[x-3]의 관계를 사용한다.
* 여기서 dp[x]가 의미하는 것은 x를 1,2,3의 합으로 표현하는 방법의 수
* dp[x] = dp[x-1]+dp[x-2]+dp[x-3]의 관계가 성립하는 것을 알 수 있다.
* 여기서 낮은 인덱스부터 dp를 채워가며 진행한다. 점화식이 제대로 작동하려면 lower number dp가 완성되어 있어야 하기 때문이다.
* exception 처리는 아래 코드를 보면 됩니다.

## Code

```python
def solution():
    n = int(input())
    def body():
        m = int(input())
        dp = [0]*((3 if m<4 else m)+1)
        dp[1]=1
        dp[2]=2
        dp[3]=4
        if m<4:
            print(dp[m])
            return
        for i in range(4, m+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        print(dp[-1])
        
    for _ in range(n):
        body()
solution()
```

{baekjoon, {1100, string}}

## 백준 1100 하얀 칸

### [문제](https://www.acmicpc.net/problem/1100)
 
### 코드

```python
def solution():
    answer = 0
    for i in range(8):
      a = input().rstrip()
      for j, e in enumerate(a):
            if e == 'F' and i%2 == j%2 : ## 이 부분이 그나마 코드 한 줄이라도 줄여준 부분
                answer +=1
    print(answer) 
solution()
```

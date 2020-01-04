{baekjoon, {1120, string}}

## 백준 1120 문자열

### [문제](https://www.acmicpc.net/problem/1120)
 
### 접근법

* sliding window기법을 사용하였다.

```python
def solution():
    A,B = input().rstrip().split()
    answer = []
    for i in range(len(B)-len(A)+1):
        answer.append(sum([1 if a != b else 0 for a,b in zip(A,B[i:i+len(A)])]))
    print(min(answer))

solution()
```

{baekjoon, {1032, string}}

## 백준 1032 명령 프롬프트

### [문제](https://www.acmicpc.net/problem/1032)

### 접근법1

* 첫번째 문자열을 가리키는 result 변수를 준비한다. 즉, 첫번째 문자열이 담겨 있다.

* 이제 비교를 한다.
* 우선, 첫번째 문자열과 두번째 문자열과 비교하는데, 한 자리씩 비교한다.
    * 같은 위치의 문자가 같다면 그대로 두고, 같지 않다면 해당 자리의 문자를 ?로 치환한다.
* 이러한 방식대로 첫번째 문자열과 n번째 문자열을 비교하며 끝가지 가면 result가 완성된다.

```python
n = int(input())
words = []
for _ in range(n):
    words.append(input())

m = len(words[0])
answer = list(words[0])
for i in range(m):
    for j in range(1, n):
        if answer[i] != words[j][i]:
            answer[i] = '?'
    
print(''.join(answer))

```

### 접근법 2

* zip과 set을 이용한 방법
* 같은 자리에 있는 녀석들을 모아서 set로 만들었을때, set의 크기가 1이면 모두 같은 문자, 아니면 ?로 가야지

```python
def solution():
    n = int(input())
    words=[]
    for _ in range(n):
        words.append(input().rstrip())
    result = []
    for t in list(zip(*words)):
        if len(set(t)) == 1:
            result.append(t[0])
        else:
            result.append('?')
    print("".join(result))
```




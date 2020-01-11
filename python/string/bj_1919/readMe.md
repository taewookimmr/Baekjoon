{baekjoon, {1919, string}}

## 백준 1919 애너그램 만들기

### [문제](https://www.acmicpc.net/problem/1919)
 
### 접근법

* dictionary를 사용하였다.
    * key-value : 알파벳-갯수

* 두 개의 dictionary를 준비한다.
    * 한 dictionary의 키와 다른 dictionary의 키가 같다면 그 value값 중에서 작은 값(갯수) 만큼 (최종적으로) 남게 된다.

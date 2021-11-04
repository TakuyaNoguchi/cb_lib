# 約数の列挙

Nの約数を列挙する場合、1 ～ sqrt(N)の各値(= n)について、

1. N が n で割り切れる場合 -> n
2. 1に該当し かつ N / n が n ではない場合 -> N / n

の1, 2を格納した配列が約数の一覧となる。

以下にサンプルコードを記載する。

```python
import math

N = int(input())
answer = []

for n in range(1, int(math.sqrt(N)) + 1):
    if N % n == 0:
        answer.append(n)

        if N // n != n:
            answer.append(N // n)

print("\n".join(map(str, sorted(answer))))
```
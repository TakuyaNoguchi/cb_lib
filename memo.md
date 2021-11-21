# 最大値

* int
  * sys.maxsize
  * ただしPython3ではint型に上限はないため、sys.maxsizeを超える値を設定可能
    * https://note.nkmk.me/python-inf-usage/
* float
  * float('INF')

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

# x軸で反射(入射角、反射角が同じ)

(Sx, Sy) -> x軸で反射 -> (Gx, Gy) の場合、Sy : Gy に内分する点でx軸で交わる。

Sx -> Gx への変化について Sy : Gy に内分するx座標は (Sx * Gy + Gx * Sy) / (Sy + Gy) で求めることが出来る。

https://atcoder.jp/contests/abc183/editorial/287

# bit探索

2**(N-1)通り、全探索が可能となる。

```python
for bit in product((True, False), repeat=N - 1):
```

https://qiita.com/u2dayo/items/90de677aa7a9b21b683b#%E5%AE%9F%E8%A3%85-2

# mod逆元

(a + b) mod M ≡ (a mod M) + (b mod M)
(a - b) mod M ≡ (a mod M) - (b mod M)
(a * b) mod M ≡ (a mod M) * (b mod M)

https://www.creativ.xyz/modulo-basic/

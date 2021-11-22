# 数学

## 最大値

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

## x軸で反射(入射角、反射角が同じ)

(Sx, Sy) -> x軸で反射 -> (Gx, Gy) の場合、Sy : Gy に内分する点でx軸で交わる。

Sx -> Gx への変化について Sy : Gy に内分するx座標は (Sx * Gy + Gx * Sy) / (Sy + Gy) で求めることが出来る。

https://atcoder.jp/contests/abc183/editorial/287

## bit探索

2**(N-1)通り、全探索が可能となる。

```python
for bit in product((True, False), repeat=N - 1):
```

https://qiita.com/u2dayo/items/90de677aa7a9b21b683b#%E5%AE%9F%E8%A3%85-2

## mod逆元

(a + b) mod M ≡ (a mod M) + (b mod M)
(a - b) mod M ≡ (a mod M) - (b mod M)
(a * b) mod M ≡ (a mod M) * (b mod M)

https://www.creativ.xyz/modulo-basic/

## 三角形の成立条件

長さが a, b, c の辺について、

  |a - c| < c < a + b

が成り立つ場合、三角形が作成できる。

http://physics.thick.jp/Mathematics_A/Section5/5-3.html#:~:text=2%E3%81%A4%E3%81%AE%E8%BE%BA%E3%81%AE%E9%95%B7,%E3%81%AE%E9%95%B7%E3%81%95%E3%82%88%E3%82%8A%E7%9F%AD%E3%81%8F%E3%81%AA%E3%82%8B%E3%80%82

# Python

## 正規表現を使った検索

re.search を使うようにする(re.match は文字列の先頭がマッチするかを調べるため)。

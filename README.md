# atcoder

- [atcoder](#atcoder)
  - [環境](#%e7%92%b0%e5%a2%83)
  - [オーダー](#%e3%82%aa%e3%83%bc%e3%83%80%e3%83%bc)
  - [便利](#%e4%be%bf%e5%88%a9)
  - [Python の list などのオーダー](#python-%e3%81%ae-list-%e3%81%aa%e3%81%a9%e3%81%ae%e3%82%aa%e3%83%bc%e3%83%80%e3%83%bc)
  - [pypy じゃだめらしい](#pypy-%e3%81%98%e3%82%83%e3%81%a0%e3%82%81%e3%82%89%e3%81%97%e3%81%84)
  - [定数倍高速化](#%e5%ae%9a%e6%95%b0%e5%80%8d%e9%ab%98%e9%80%9f%e5%8c%96)
  - [2 重ループ](#2-%e9%87%8d%e3%83%ab%e3%83%bc%e3%83%97)

## 環境

conda activate atcoder

pypy3 nanka.py

## オーダー

Python で乗るのは 10\*\*6 くらいまで

## 便利

- 標準入力にはリダイレクトで渡せる

```
python spam.py < sample.txt
```

## Python の list などのオーダー

- del は o(n)なので使わない, 新しく配列作ったほうが速い
- in も list では o(n), set, dict に直す
-

## pypy じゃだめらしい

- 再帰
- dict
- 文字
- deque
- 内包表記　(ベタ書きの方が速いらしい)

## 定数倍高速化

- enumerate
- 小さいループを外に
- .をなくす

```python
r_append = res.append

for i in range(n):
    r_append(1)
```

## 2 重ループ

- flag を使う: こっちのほうが絶対わかりやすい

```python
flag = False
for i in l1:
    for j in l2:
        print(i, j)
        if i == 2 and j == 20:
            flag = True
            print('BREAK')
            break
    if flag:
        break
```

- continue, else を 使う: 分かるけどわかりにくい

```python
for i in l1:
    for j in l2:
        print(i, j)
        if i == 2 and j == 20:
            print('BREAK')
            break
    else:
        continue # break が呼ばれなければ そとの for文を続ける

    break # continue されなければ 外のループもbreak
```

- itertools.product()はループ数が増えるので使わないべき

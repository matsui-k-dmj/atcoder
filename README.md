# atcoder
- [atcoder](#atcoder)
  - [便利](#%E4%BE%BF%E5%88%A9)
  - [Python の list などのオーダー](#Python-%E3%81%AE-list-%E3%81%AA%E3%81%A9%E3%81%AE%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC)
  - [pypy じゃだめらしい](#pypy-%E3%81%98%E3%82%83%E3%81%A0%E3%82%81%E3%82%89%E3%81%97%E3%81%84)
  - [定数倍高速化](#%E5%AE%9A%E6%95%B0%E5%80%8D%E9%AB%98%E9%80%9F%E5%8C%96)
  - [2重ループ](#2%E9%87%8D%E3%83%AB%E3%83%BC%E3%83%97)
## 便利

- 標準入力にはリダイレクトで渡せる
```
python spam.py < sample.txt
```

## Python の list などのオーダー
- del は o(n)なので使わない, 新しく配列作ったほうが速い
- in も listではo(n), set, dictに直す
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

## 2重ループ

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

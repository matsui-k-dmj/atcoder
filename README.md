# atcoder

- [atcoder](#atcoder)
  - [やり方](#やり方)
  - [Python Tips](#python-tips)
    - [オーダー](#オーダー)
    - [便利](#便利)
    - [Python の list などのオーダー](#python-の-list-などのオーダー)
    - [pypy では遅いもの](#pypy-では遅いもの)
    - [定数倍高速化](#定数倍高速化)
    - [2 重ループ](#2-重ループ)

## やり方

- 環境
  `poetry shell`

- コンペ前

  - Template フォルダをコピペして rename する
  - そのフォルダに入っとく

- テスト

  - chrome 拡張 Atcoder Unit Test で 貼り付ける.
  - AtCoder Unit Test で自動生成できる, 最後の unittest.main は消す
  - python -m unittest template/template.py
  - pypy3 -m unittest template/template.py

- プロファイリング

  - テスト用のデータは adhok に作る python D_data.py > D_data.txt とか
  - 関数に @profile デコレータをつける。終わったらコメントアウトする
  - kernprof -l D.py < test_D_input_4.txt
  - python -m line_profiler D.py.lprof

- 復習
  - 使ったアルゴリズムを docstrings に書いて、後でググれるようにする
  - もし関数化したほうが良さそうなら、Algo に入れる

## Python Tips

### オーダー

Python で乗るのは 10\*\*6 くらいまで

### 便利

- 標準入力にはリダイレクトで渡せる

```
python spam.py < sample.txt
```

### Python の list などのオーダー

- del は o(n)なので使わない, 新しく配列作ったほうが速い
- in も list では o(n), set, dict に直す
-

### pypy では遅いもの

- 再帰
- dict
- 文字
- deque
- 内包表記　(ベタ書きの方が速いらしい)

### 定数倍高速化

- enumerate
- 小さいループを外に
- .をなくす

```python
r_append = res.append

for i in range(n):
    r_append(1)
```

### 2 重ループ

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

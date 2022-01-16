# atcoder

https://atcoder.jp/users/Kazhir

- [atcoder](#atcoder)
  - [やり方](#やり方)
  - [Python Tips](#python-tips)
    - [オーダー](#オーダー)
    - [入力](#入力)
    - [Python の list などのオーダー](#python-の-list-などのオーダー)
    - [pypy では遅いもの](#pypy-では遅いもの)

## やり方

- 実行

source .venv/Scripts/activate

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

## Python Tips

### オーダー

Python で通るのは 10\*\*6 くらいまで

### 入力

- 標準入力にはリダイレクトで渡せる

```
python spam.py < sample.txt
```

- stdin.readline

input に比べて速い。
sys.stdin.readline は最後に改行文字 \n が入る  
split は スペースで区切るのと、\n を削除する. スペースが無い場合は要素 1 個のリストを返す

### Python の list などのオーダー

- del は o(n)なので使わない, 新しく配列作ったほうが速い
- in も list では o(n), set, dict に直す

### pypy では遅いもの

pypy のバージョンが上がってだいぶ改善されてる

- 再帰
- dict
- 文字
- deque
- 内包表記 (ベタ書きの方が速いらしい)

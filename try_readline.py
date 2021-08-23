"""
sys.stdin.readlineは最後に改行文字 \n が入る
split は スペースで区切るのと、\nを削除する. スペースが無い場合は要素1個のリストを返す
"""
import sys

readline = sys.stdin.readline
s = readline()
print(list(s))
print(s.split())
print(s.split()[0])

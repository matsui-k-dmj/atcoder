```
pip install line_profiler
```

関数に @profile デコレータをつける。これはコメントアウトするべき

kernprof -l ABC134/D.py < test_D_input_4.txt
python -m line_profiler D.py.lprof
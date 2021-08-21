Total time: 27.2377 s
File: ABC134/D.py
Function: resolve at line 11

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    11                                           @profile
    12                                           def resolve():
    13         1         16.0     16.0      0.0      N = [int(x) for x in sys.stdin.readline().split()][0]
    14         1       3231.0   3231.0      0.0      a_list = [int(x) for x in sys.stdin.readline().split()]
    15                                           
    16         1      14556.0  14556.0      0.1      logger.debug('{} {}'.format(N, a_list))
    17                                           
    18         1       1239.0   1239.0      0.0      box_list = [0 for _ in range(N)]
    19                                           
    20     20001      11332.0      0.6      0.0      for i in reversed(range(N)):
    21     20000      11878.0      0.6      0.0          k = i + 1
    22     20000   27167049.0   1358.4     99.7          suma = sum([box_list[j] for j in range(k, N) if (j + 1) % k])
    23                                           
    24     20000      13839.0      0.7      0.1          r = suma % 2
    25     20000      12803.0      0.6      0.0          if r != a_list[i]:
    26        80         58.0      0.7      0.0              box_list[i] = 1
    27                                           
    28         1         72.0     72.0      0.0      s = sum(box_list)
    29         1         29.0     29.0      0.0      print(s)
    30                                           
    31         1          1.0      1.0      0.0      if s > 0:
    32         1          1.0      1.0      0.0          print(' '.join(
    33         1       1585.0   1585.0      0.0              [str(i + 1) for i in range(len(box_list)) if box_list[i]]))
"""heapq使っても自作Heapと全然速度かわらん
heapq は 最小値が前
"""
import heapq


class Heapq:
    def __init__(self, _list=None):
        if _list is not None:
            self.heap = _list
            heapq.heapify(self.heap)
        else:
            self.heap = []

    def pop(self):
        return heapq.heappop(self.heap)

    def push(self, x):
        heapq.heappush(self.heap, x)


class MyHeap:
    def __init__(self, _list=None):
        self.heap = []
        if _list is not None:
            for x in _list:
                self.push(x)

    def pop(self):
        if len(self.heap) == 0:
            return
        elif len(self.heap) == 1:
            return self.heap.pop(0)
        retval = self.heap[0]

        self.heap[0] = self.heap.pop(-1)

        i_parent = 0
        while True:
            is_updated = False
            i_left = 2 * i_parent + 1
            i_right = 2 * i_parent + 2

            # 境界条件
            if i_left >= len(self.heap):
                break
            elif i_right >= len(self.heap):
                i_right = i_left

            # 子供の小さいほうと交代
            if self.heap[i_left] < self.heap[i_right]:
                i_replace = i_left
            else:
                i_replace = i_right

            # 交代
            if self.heap[i_replace] < self.heap[i_parent]:
                is_updated = True
                self.heap[i_parent], self.heap[i_replace] = (
                    self.heap[i_replace],
                    self.heap[i_parent],
                )
                i_parent = i_replace

            if not is_updated:
                break

        return retval

    def push(self, x):
        self.heap.append(x)

        i_self = len(self.heap) - 1

        while True:
            is_updated = False
            i_parent = (i_self - 1) // 2

            # 境界
            if i_parent < 0:
                break

            # 親が自分より小さければ交代
            if self.heap[i_parent] > self.heap[i_self]:
                is_updated = True

                self.heap[i_parent], self.heap[i_self] = (
                    self.heap[i_self],
                    self.heap[i_parent],
                )

                i_self = i_parent

            if not is_updated:
                break

    def drain(self):
        while self.heap:
            yield self.pop()

class Heap:
    def __init__(self, x_list=None):
        if x_list is None:
            x_list = []
        self.heap = []
        for x in x_list:
            self.push(x)

    def push(self, x):
        self.heap.append(x)

        i = len(self.heap) - 1
        while (i > 0):
            pi = (i - 1) // 2
            child = self.heap[i]
            parent = self.heap[pi]
            if parent > child:  # 入れ替える
                self.heap[pi] = child
                self.heap[i] = parent
            i = pi

    def pop(self):
        if len(self.heap) == 0:
            return
        elif len(self.heap) == 1:
            return self.heap.pop(0)
        to_pop = self.heap[0]

        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)

        i = 0
        while (True):
            parent = self.heap[i]
            i_child1 = i * 2 + 1
            i_child2 = i * 2 + 2
            if i_child1 < len(self.heap):
                child1 = self.heap[i_child1]
            else:
                break  # no more child

            if i_child2 < len(self.heap):
                child2 = self.heap[i_child2]
                if child1 < child2:
                    i_child = i_child1

                else:
                    i_child = i_child2

            else:
                i_child = i_child1

            child = self.heap[i_child]
            if child < parent:  # swap
                self.heap[i] = child
                self.heap[i_child] = parent
                i = i_child

        return to_pop

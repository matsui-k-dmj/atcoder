# AVL tree
# see: AVL tree implementation in python · GitHub https://gist.github.com/girish3/a8e3931154af4da89995#file-avl_tree-py-L12
# see: python AVL木 配列ver 　競技プログラミング　Atcoder - じゅっぴーダイアリー https://juppy.hatenablog.com/entry/2019/02/26/python_AVL%E6%9C%A8_%E9%85%8D%E5%88%97ver_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder_


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def search(self, key):
        """keyがあればkeyを返す。なければNone
        
        Args:
            key ([type]): [description]
        
        Returns:
            [type]: [description]
        """
        if self.node == None:  # 1要素も無いとき
            return

        if self.node.key == None:
            return None
        if self.node.key > key:
            if self.node.left.node == None:
                return None
            else:
                return self.node.left.search(key)
        if self.node.key < key:
            if self.node.right.node == None:
                return None
            else:
                return self.node.right.search(key)
        return self.node.key  # self.node.key == keyの場合

    def insert(self, key):
        tree = self.node

        newnode = Node(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        self.rebalance()

    def erase(self, key):
        if self.node != None:
            if self.node.key == key:
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None:  # sanity check
                        self.node.key = replacement.key

                        # replaced. Now erase the key from right child
                        self.node.right.erase(replacement.key)

                self.rebalance()
                return
            elif key < self.node.key:
                self.node.left.erase(key)
            elif key > self.node.key:
                self.node.right.erase(key)

            self.rebalance()
        else:
            return

    def ex_upper_bound(self, ub, key_lower=None):
        """ub がexclusiveなupper bound.
        つまり、ub より小さい最大の値を返す。なければNone
        
        Args:
            ub (int): exclusiveなupper bound
            key_lower ([type], optional): [description]. Defaults to None.
        
        Returns:
            int: keyより小さい最大の値
        """
        if self.node == None:  # 1要素も無いとき
            return

        if self.node.key == None:
            return key_lower

        if self.node.key > ub:  # ノードの方がub より大きいので左に行く
            if self.node.left.node == None:
                return key_lower
            else:
                return self.node.left.ex_upper_bound(ub, key_lower)

        if self.node.key < ub:  # ノードの方が ub より 小さいので右に行く
            key_lower = self.node.key
            if self.node.right.node == None:
                return key_lower
            else:
                return self.node.right.ex_upper_bound(ub, key_lower)

        #self.node.key == ubの場合
        if self.node.left.node == None:
            return key_lower
        else:  # left以下のもっとも高い数値とkey_lowerのもっとも高いほう
            if key_lower == None:
                return self.logical_predecessor(self.node).key
            else:
                return max(key_lower, self.logical_predecessor(self.node).key)

    def ex_lower_bound(self, lb, key_upper=None):
        """lb がexclusiveなlower bound.
        つまり、lb より大きい最小の値を返す。なければNone
        
        Args:
            lb (int): exclusiveなlower bound.
            key_higher ([type], optional): [description]. Defaults to None.
        
        Returns:
            int: keyより大きい最小の値を返す
        """
        if self.node == None:  # 1要素も無いとき
            return
        if self.node.key == None:
            return key_upper
        if self.node.key > lb:
            key_upper = self.node.key
            if self.node.left.node == None:
                return key_upper
            else:
                return self.node.left.ex_lower_bound(lb, key_upper)
        if self.node.key < lb:
            if self.node.right.node == None:
                return key_upper
            else:
                return self.node.right.ex_lower_bound(lb, key_upper)
        #self.node.key == lbの場合
        if self.node.right.node == None:
            return key_upper
        else:
            if key_upper == None:
                return self.logical_successor(self.node).key
            else:
                return min(key_upper, self.logical_successor(self.node).key)

    def is_leaf(self):
        return (self.height == 0)

    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def logical_predecessor(self, node):
        """Find the biggest valued node in LEFT child
        
        Args:
            node (Node): [description]
        
        Returns:
            Node: the biggest valued node in LEFT child
        """
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        """Find the smallest valued node in RIGHT child
        
        Args:
            node (Node): [description]
        
        Returns:
            Node: the smallest valued node in RIGHT child
        """
        node = node.right.node
        if node != None:  # just a sanity check

            while node.left != None:
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced()
                and self.node.right.check_balanced())

    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if (self.node != None):
            print('-' * level * 2, pref, self.node.key,
                  "[" + str(self.height) + ":" + str(self.balance) + "]",
                  'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')


##################################################################################
class node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data == None:
            self.data = data
            return

        elif data < self.data:
            if (self.left != None):
                self.left.insert(data)
                return
            else:
                self.left = node(data)
                return

        else:
            if self.right != None:
                self.right.insert(data)
                return
            else:
                self.right = node(data)
                return

    def get_min(self):
        par = None
        cur = self
        while cur.left != None:
            par = cur
            cur = cur.left
        print(cur.data)

        if cur == self:
            if cur.right != None:
                temp_right = self.right
                self.data = temp_right.data
                self.left = temp_right.left
                self.right = temp_right.right
            else:
                self.data = None
                self.left = None
                self.right = None
        else:
            if cur.right != None:
                par.left = cur.right
            else:
                par.left = None

    def get_max(self):
        par = None
        cur = self
        while cur.right != None:
            par = cur
            cur = cur.right
        print(cur.data)

        if cur == self:
            if cur.left != None:
                temp_left = self.left
                self.data = temp_left.data
                self.left = temp_left.left
                self.right = temp_left.right
            else:
                self.data = None
                self.left = None
                self.right = None
        else:
            if cur.left != None:
                par.right = cur.left
            else:
                par.right = None

    # def show(self):
    #     if (self.left != None):
    #         self.left.show()

    #     print(self.data, end=" ")

    #     if (self.right != None):
    #         self.right.show()
        

n = int(input())
myBST = node()
for i in range(n):
    l = input().split()

    if l[0] == "1":
        x = int(l[1])
        myBST.insert(x)

    elif l[0] == "2":
        myBST.get_min()

    elif l[0] == "3":
        myBST.get_max()

    # print("+++++++++++", end=" ")
    # myBST.show()
    # print()

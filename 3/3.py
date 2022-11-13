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

    def closest(self, x, min):
        if x == self.data:
            return 0
        temp = abs(x-self.data)

        if x < self.data:
            if self.left == None:
                if min < temp:
                    return min
                return temp
            else:
                _temp_ = self.left.closest(x, temp)
                if _temp_ < temp:
                    return _temp_
                return temp

        else:
            if self.right == None:
                if min < temp:
                    return min
                return temp
            else:
                _temp_ = self.right.closest(x, temp)
                if _temp_ < temp:
                    return _temp_
                return temp

n = int(input())
myBST = node()
for i in range(n):
    l = input().split()
    cmd = l[0]
    x = int(l[1])
    if cmd == "1":
        myBST.insert(x)
    elif cmd == "2":
        print(myBST.closest(x, abs(x-myBST.data)))
    
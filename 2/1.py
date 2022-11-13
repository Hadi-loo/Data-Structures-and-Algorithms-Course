a = input().split(",")
n = int(a[0])
word = a[1]
_map_ = []
x_delta = [-1, -1, -1, 0, 1, 1, 1, 0]
y_delta = [1, 0, -1, -1, -1, 0, 1, 1]
for k in range(n):
    _map_.append(input().split(","));


def func(key, x, y, _str_):
    if len(key) == 1:
        print(_str_)
        return
    for i in range(8):
        new_x = x + x_delta[i]
        new_y = y + y_delta[i]
        if (new_x >= 0) and (new_x < n) and (new_y >= 0) and (new_y < n):
            if _map_[new_x][new_y] == key[1]:
                if ("(" + str(new_x) + ", " + str(new_y) + ")") not in _str_:
                    func(key[1:], new_x, new_y, _str_ + "," + "(" + str(new_x) + ", " + str(new_y) + ")")


for w in range(n):
    for z in range(n):
        if _map_[w][z] == word[0]:
            func(word, w, z, "(" + str(w) + ", " + str(z) + ")")

s = input()
out = []
for ch in s:
    if len(out) == 0:
        out.append(ch)
    else:
        if out[-1] == ch:
            out.pop()
        else:
            out.append(ch)

for ch in out:
    print(ch, end="")

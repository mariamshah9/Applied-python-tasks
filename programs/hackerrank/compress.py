from itertools import *

no = input()
m = list()

l = [list(g) for k, g in groupby(no)]
for i in l:
    t = []
    t.append(len(i))
    t.append(int(i[0]))
    t = tuple(t)
    m.append(str(t))


if __name__ == '__main__':
    print (' '.join(m))

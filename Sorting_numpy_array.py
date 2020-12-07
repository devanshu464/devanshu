import numpy as np
l = [[10,80,5],[80,95,2],[5,4,-1]]
a = np.array(l)
print(a)
print()
b = np.sort(a)
print(b)
print()
c = np.sort(a, axis = 0)
print(c)

d= np.sort(a, axis = 0,kind = "mergesort")
print(d)
print()

e = np.sort(a, axis = 0, kind = "quicksort")
print(e)
print()
f = np.sort(a, axis = 0, kind = "heapsort")
print(f)
print()
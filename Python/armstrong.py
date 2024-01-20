a = 153
b = [int(x) for x in str(a)]
print(b)
c = 0
for i in range(len(b)):
    c += b[i]**3
if c == a:
    print(True)
else:
    print(False)
    
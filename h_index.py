citations = [3,0,6,1,5]

citations = sorted(citations, reverse=True)
h = 0
for n, i in enumerate(citations):
    if i >= n + 1:
        h = h + 1
    else:
        break
print(h)


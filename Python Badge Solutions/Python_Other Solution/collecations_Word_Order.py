from collections import Counter
N = int(input())
wrd = Counter([input() for i in range(N)])
print(str(len(wrd)))
print(*wrd.values())

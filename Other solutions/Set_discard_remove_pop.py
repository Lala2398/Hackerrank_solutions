n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    inp = input().split()
    if inp[0] == "pop":
        s.pop()
    elif inp[0] == "remove":
        s.remove(int(inp[1]))
    elif inp[0] == "discard":
        s.discard(int(inp[1]))
print(sum(s))



# elif Covers All Cases: The elif statements effectively cover all possible valid input scenarios. 
#If the input is not "pop," it checks if it's "remove," and if not that, it checks if it's "discard." 
#If it's none of these, then it's an invalid command (which is not handled in this code but could be in a more robust implementation).

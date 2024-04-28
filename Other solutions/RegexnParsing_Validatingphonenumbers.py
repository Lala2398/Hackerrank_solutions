import re

test_case = int(input())

for i in range(test_case):
    
    match = re.match(r"^[789]{1}[\d]{9}$", input())

    if match:
        print("YES")
    else:
        print("NO")

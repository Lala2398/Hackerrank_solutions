if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_1 = set(arr)
    arr_1.remove(max(arr_1))
    print(max(arr_1))

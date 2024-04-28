eng= int(input())
set_eng=set(map(int, input().split()))
fr= int(input())
set_fr=set(map(int, input().split()))

print(len(set_eng.union(set_fr)))

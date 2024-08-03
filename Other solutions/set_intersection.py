n_eng = int(input().strip())
eng_subs = set(map(int, input().strip().split()))

n_fr = int(input().strip())
fr_subs = set(map(int, input().strip().split()))

print(len(eng_subs & fr_subs))

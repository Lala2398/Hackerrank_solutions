if __name__ == '__main__':
    list = []
    for i in range(int(input())):
        names = input()
        scores = input()
        list.append([names, scores])
second_highest = sorted(set([scores for names, scores in list]))[1]
print('\n'.join(sorted([names for names, scores in list if scores == second_highest])))

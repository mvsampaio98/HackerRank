if __name__ == '__main__':
    lista = []
    only_score = []
    only_name = []
    second_low = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name,score])
        only_score.append(score)
    only_score = sorted(set(only_score))
    second_low = only_score[1]
    for i in lista:
        if second_low==i[1]:
            only_name.append(i[0])
    only_name.sort()
    for j in only_name:
        print(j)

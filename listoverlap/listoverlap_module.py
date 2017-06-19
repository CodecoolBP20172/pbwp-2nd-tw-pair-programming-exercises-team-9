from random import randint

def listoverlap(list1, list2):
    return list(set(list1) & set(list2))


def main():
    lista = []
    listb = []
    for i in range(randint(1, 100)):
        lista.append(randint(1, 101))

    for i in range(randint(1, 100)):
        listb.append(randint(1, 101))

    # print(lista)

    return list(set(lista) & set(listb))


if __name__ == '__main__':
    main()

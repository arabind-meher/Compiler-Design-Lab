if __name__ == '__main__':
    s = input('Enter Non-Terminals who have left recursions: ')
    n = len(s)
    d = {}
    l = []

    for i in s:
        a = input('\nEnter the production for {}: '.format(i))
        d[i] = a

    print('\nBefore Eliminating Left Factoring')
    for i in s:
        a = d[i]
        l = a.split()

        p = i + ' -> ' + ' | '.join(l)
        print(p)

    print('\nAfter Eliminating Left Factoring')
    for i in s:
        a = d[i]
        l = a.split()
        n = len(l)
        t = ''
        m = 0

        for j in l:
            if m > len(j):
                m = len(j)

        for j in range(m):
            if l[0][j] == l[1][j]:
                t = t + l[0][j]
            else:
                break

        p = i + ' -> ' + t + i + "'"
        p(p)

        if len(l[0][j:]) == 0:
            l0 = u'\u03B5'
        else:
            l0 = l[0][j:]

        if len(l[1][j:]) == 0:
            l1 = u'\u03B5'
        else:
            l1 = l[1][j:]

        p = i + ' -> ' + l0 + ' | ' + l1
        print(p)

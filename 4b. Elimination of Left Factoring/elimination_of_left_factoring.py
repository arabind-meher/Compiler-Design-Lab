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
        m = 100

        for j in l:
            if m > len(j):
                m = len(j)
                t = j

        while True:
            f = 1
            for j in l:
                if t not in j:
                    f = 0
                    break
            if f == 1:
                break
            else:
                m = m - 1
                if m == 0:
                    t = ''
                    break
                t = t[0:m]
        k = len(t)

        p = i + ' -> ' + t + i + "'"
        print(p)

        p = i + "' -> "
        p0 = []

        for j in l:
            if len(j[k:]) == 0:
                l0 = u'\u03B5'
            else:
                l0 = j[k:]

            p0.append(l0)

        p = p + ' | '.join(p0)
        print(p)

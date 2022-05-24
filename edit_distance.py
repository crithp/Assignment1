

def min_edit_distance(target, source, ins_cost=1, del_cost=1, sub_cost=2):

    def fsub_cost(x, y):
        if x == y:
            return 0
        return sub_cost

    def fins_cost(x):
        return ins_cost

    def fdel_cost(x):
        return del_cost

    n = len(target)
    m = len(source)

    distance = [[0 for x in range(m + 1)] for y in range(n + 1)]

    for i in range(1, n+1):
        distance[i][0] = distance[i-1][0] + fins_cost(target[i - 1])

    for i in range(1, m+1):
        distance[0][i] = distance[0][i-1] + fdel_cost(source[i - 1])

    for i in range(1, n+1):
        for j in range(1, m + 1):
            distance[i][j] = min([
                distance[i - 1][j] + fins_cost(target[i - 1]),
                distance[i][j - 1] + fdel_cost(source[j - 1]),
                distance[i - 1][j - 1] + fsub_cost(source[j - 1], target[i - 1])
            ])

    return distance


if __name__ == '__main__':
    source = input("Please enter source word: ")
    target = input("Please enter target word: ")
    ins_cost = input("Please enter insert cost (default 1): ")
    del_cost = input("Please enter deletion cost (default 1): ")
    sub_cost = input("Please enter substitution cost (default 2): ")

    ins_cost = 1 if ins_cost == '' else int(ins_cost)
    del_cost = 1 if del_cost == '' else int(del_cost)
    sub_cost = 2 if sub_cost == '' else int(sub_cost)

    d = min_edit_distance(target, source, ins_cost, del_cost, sub_cost)
    print("Resulting matrix:")
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in reversed(d)]))

import fractions


def solution(bananas):
    g = generate_graph(bananas)
    matches = pairs(g)
    return len(bananas) - matches


def loop(x, y):
    base = (x + y) // fractions.gcd(x, y)
    return bool(base & (base - 1))


def generate_graph(bananas):
    g = {i: [] for i in range(len(bananas))}
    for i in range(len(bananas)):
        for j in range(i, len(bananas)):
            if i != j and loop(bananas[i], bananas[j]):
                g[i].append(j)
                g[j].append(i)
    return g


def pairs(g):
    matched = 0
    checks = len(g[max(g, key=lambda key: len(g[key]))])
    while len(g) > 1 and checks >= 1:
        init_mw_node = min(g, key=lambda key: len(g[key]))
        if (len(g[init_mw_node])) < 1:
            del g[init_mw_node]
        else:
            temp_sec_min = [len(g[g[init_mw_node][0]]) + 1, 1]
            for node_i in g[init_mw_node]:
                if len(g[node_i]) < temp_sec_min[0]:
                    temp_sec_min = [len(g[node_i]), node_i]
                for check_i in range(len(g[node_i])):
                    if g[node_i][check_i] == init_mw_node:
                        del g[node_i][check_i]
                        break
            for node_i in g[temp_sec_min[1]]:
                for check_i in range(len(g[node_i])):
                    if g[node_i][check_i] == temp_sec_min[1]:
                        del g[node_i][check_i]
                        break
            del g[init_mw_node]
            del g[temp_sec_min[1]]
            matched += 2
        if len(g) > 1:
            checks = len(g[max(g, key=lambda key: len(g[key]))])
    return matched


print(solution([1, 1]))
print(solution([1, 7, 3, 21, 13, 19]))

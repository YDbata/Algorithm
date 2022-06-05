from itertools import combinations,  product, permutations


def solution(n, weak, dist):
    answer = 0
    loc = [-1, 1]
    for i in range(1, len(dist) + 1):

        choice = list(permutations(dist, i))
        choice_w = list(permutations(weak, i))
        loc_l = list(product(loc, repeat = i))
        # print(choice, loc_l, choice_w)
        # print(*choice, sep=" ")
        for c in choice:
            for w in choice_w:
                # print(c, w)
                for l in loc_l:
                    # print(l)
                    new_weak = weak.copy()
                    for cs in range(len(c)):
                        for c2 in range(c[cs] + 1):
                            if (w[cs] + (l[cs] * c2)) % n in new_weak:
                                # print((w[cs] + (l[cs] * c2)) % n, w[cs], l[cs], c2, new_weak)
                                new_weak.remove((w[cs] + (l[cs] * c2)) % n)
        # print(new_weak)
                    if len(new_weak) == 0:
                        return i

    return -1

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
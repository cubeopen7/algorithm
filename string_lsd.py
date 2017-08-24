# -*- coding: utf-8 -*-

import numpy as np

def char2index(c):
    return ord(c) - ord("a")


def string_lsd(data, R):
    # 默认每个字符串的长度相同
    # data: 字符串数组
    # R: 字符字母表(26, 256, 65536)
    N = len(data)
    W = len(data[0])
    aux = np.empty(N, dtype=np.str)

    for d in range(W-1, -1, -1):
        count = np.zeros(R+1, dtype=np.int8)
        for string in data:
            count[char2index(string[d])+1] += 1

        for i in range(R):
            count[i+1] += count[i]

        for string in data:
            aux[count[char2index(string[d])]] = string
            count[char2index(string[d])] += 1

        data = aux.tolist()

    return aux


if __name__ == "__main__":
    test_list = ["qwe", "asd", "zxc", "rty", "fgh", "vbn", "uio", "jkl"]
    sort_list = string_lsd(test_list, 26)
    print(sort_list)
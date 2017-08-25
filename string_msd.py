# -*- coding: utf-8 -*-

R = 26
M = 15  # 停止递归, 切换到插入排序的阈值

def char2index(s, d):
    try:
        return ord(s[d]) - ord("a")
    except Exception as e:
        return -1


def string_msd(data, low, high, d):
    if high <= low + M:
        pass  # 此处为插入排序代码
    count = [0] * (R + 2)
    aux = [""] * len(data)
    for i in range(low, high, 1):
        count[char2index(data[i], d)+2] += 1

    for r in range(R+1):
        count[r+1] += count[r]

    for i in range(low, high, 1):
        aux[count[char2index(data[i], d)+1]] = data[i]
        count[char2index(data[i], d) + 1] += 1

    for i in range(low, high, 1):
        data[i] = aux[i-low]

    for r in range(R):
        string_msd(data, low+count[r], high+count[r], d+1)


if __name__ == "__main__":
    test_list = ["qwe", "asd", "zxc", "rty", "fgh", "vbn", "uio", "jkl"]
    sort_list = string_msd(test_list, 0, len(test_list), 0)
    print(sort_list)
# -*- coding: utf-8 -*-

R = 26

def char2index(s, d):
    try:
        return ord(s[d])- ord("a")
    except Exception as e:
        return -1


def string_sort_3direction(data, low, high, d):
    if high <= low:
        return
    lt, gt = low, high
    v = char2index(data[low], d)
    i = low + 1
    while i <= gt:
        t = char2index(data[i], d)
        if v > t:
            data[i], data[lt] = data[lt], data[i]
            lt += 1
            i += 1
        elif v < t:
            data[i], data[gt] = data[gt], data[i]
            gt -= 1
        else:
            i += 1
    string_sort_3direction(data, low, lt-1, d)
    if v >= 0:
        string_sort_3direction(data, lt, gt,d+1)
    string_sort_3direction(data, gt+1, high, d)


if __name__ == "__main__":
    test_list = ["qwe", "asd", "zxc", "rty", "fgh", "vbn", "uio", "jkl"]
    string_sort_3direction(test_list, 0, len(test_list)-1, 0)
    print(test_list)
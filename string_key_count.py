# -*- coding: utf-8 -*-

import numpy as np

def key_count(data, r):
    _len = len(data)
    _count = np.zeros(r+1, dtype=int)
    _aux = [0] * _len
    # 计算出现频率
    for key in data.values():
        _count[key+1] += 1
    # 将频率转换为索引
    for i in range(r):
        _count[i+1] += _count[i]
    # 将元素分类
    for key, value in data.items():
        _aux[_count[value]] = (value, key)
        _count[value] += 1
    # 回写, 这里进行模仿
    res = []
    for item in _aux:
        res.append(item)
    return res


def key_count_less_memory(data, r):
    _count = np.zeros(r + 1, dtype=int)
    # 计算出现频率
    for string, key in data:
        _count[key+1] += 1
    # 将频率转换为索引
    for i in range(r):
        _count[i + 1] += _count[i]
    # 将元素分类
    frz_count = _count.copy()
    i = 0
    while i < len(data):
        string, key = data[i]
        _begin, _end = frz_count[key], frz_count[key+1]
        if i >= _begin and i < _end:
            i += 1
            _count[key] += 1
        else:
            swap_index = _count[key]
            data[i], data[swap_index] = data[swap_index], data[i]
            _count[key] += 1


if __name__ == "__main__":
    # test_string_list = ["qwe", "asd", "zxc", "rty", "fgh", "vbn", "uio", "jkl"]
    test_string_dict = {"qwe": 2,
                        "asd": 3,
                        "zxc": 1,
                        "rty": 2,
                        "fgh": 1,
                        "vbn": 0}
    test_string_list_tuple = [(key, value) for key, value in test_string_dict.items()]
    # sort_res = key_count(test_string_dict, 4)
    print(test_string_list_tuple)
    key_count_less_memory(test_string_list_tuple, 4)
    print(test_string_list_tuple)
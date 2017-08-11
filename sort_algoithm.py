# -*- coding: utf-8 -*-

import numpy as np


def select_sort(data):
    data_len = len(data)
    for i in range(data_len):
        min_index = i
        for j in range(i + 1, data_len):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


def insert_sort(data):
    data_len = len(data)
    for i in range(1, data_len):
        min_value = data[i]
        j = i
        while j > 0 and data[j - 1] > min_value:
            data[j] = data[j - 1]
            j -= 1
        data[j] = min_value
    return data


def shell_sort(data):
    data_len = len(data)
    h = 1
    while h < data_len // 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(1, data_len):
            j = i
            min_value = data[i]
            while j >= h and data[j - h] > min_value:
                data[j] = data[j - h]
                j -= h
            data[j] = min_value
        h = h // 3
    return data


def merge_sort(data):
    data_len = len(data)
    if data_len < 2:
        return data
    sorted_list = []
    left = merge_sort(data[:data_len // 2])
    right = merge_sort(data[data_len // 2:])
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    if len(left) > 0:
        sorted_list.extend(left)
    else:
        sorted_list.extend(right)
    return sorted_list


def merge_sort_2(data):
    # 自底向上的归并排序
    data_len = len(data)
    sz = 1
    while sz < data_len:
        for i in range(0, data_len - sz, 2 * sz):
            sorted_list = []
            left = data[i: i + sz]
            right = data[i + sz: min(i + 2 * sz, data_len)]
            while len(left) > 0 and len(right) > 0:
                if left[0] < right[0]:
                    sorted_list.append(left.pop(0))
                else:
                    sorted_list.append(right.pop(0))
            if len(left) > 0:
                sorted_list.extend(left)
            else:
                sorted_list.extend(right)
            data[i: min(i + 2 * sz, data_len)] = sorted_list
        sz += sz
    return data


def quick_sort(data, low, high):
    data_len = len(data)
    if low >= high:
        return
    i = low
    j = high
    middle = data[low]
    while True:
        i += 1
        while data[i] < middle:
            i += 1
            if i == high - 1:
                break
        j -= 1
        while data[j] > middle:
            j -= 1
            if j == low:
                break
        if i >= j:
            break
        data[i], data[j] = data[j], data[i]
    data[low], data[j] = data[j], data[low]
    quick_sort(data, low, j)
    quick_sort(data, j + 1, high)
    return data


def heap_sort(data):
    def _sink(a, k, N):
        while 2 * k < N - 1:  # 如果存在子节点
            j = 2 * k + 1  # 左子节点
            if j < N - 1 and a[j] < a[j+1]:  # 存在右子节点, 且右子节点比左子节点大
                j += 1
            if a[k] >= a[j]:
                break
            a[k], a[j] = a[j], a[k]
            k = j

    data_len = len(data)
    # 1. 构建最大堆
    i = data_len // 2 - 1
    while i >= 0:
        _sink(data, i, data_len)
        i -= 1
    # 2. 每次拿走堆顶元素, 与剩余的最后一个元素交换, 重新对堆进行排序
    data_len -= 1
    while data_len > 0:
        data[0], data[data_len] = data[data_len], data[0]  # 交换
        _sink(data, 0, data_len)
        data_len -= 1
    return data


def heap_sort_descend(data):
    def _sink(a, k, N):
        raw = k
        left = 2 * k + 1
        right = 2 * k + 2
        if left < N and a[k] > a[left]:
            k = left
        if right < N and a[k] > a[right]:
            k = right
        if k != raw:
            a[k], a[raw] = a[raw], a[k]
            _sink(a, k, N)

    data_len = len(data)
    # 1. 构建最大堆
    i = data_len // 2 - 1
    while i >= 0:
        _sink(data, i, data_len)
        i -= 1
    # 2. 每次拿走堆顶元素, 与剩余的最后一个元素交换, 重新对堆进行排序
    data_len -= 1
    while data_len > 0:
        data[0], data[data_len] = data[data_len], data[0]  # 交换
        _sink(data, 0, data_len)
        data_len -= 1
    return data


if __name__ == "__main__":
    N = 25
    sort_list = np.random.randint(N, size=N)
    print("Raw array: {}".format(sort_list))
    # print("Select sort: {}".format(select_sort(sort_list)))
    # print("Insert sort: {}".format(insert_sort(sort_list)))
    # print("Shell sort: {}".format(shell_sort(sort_list)))
    # print("Merge sort: {}".format(np.array(merge_sort(list(sort_list)))))
    # print("Merge2 sort: {}".format(np.array(merge_sort_2(list(sort_list)))))
    # print("Quick sort: {}".format(quick_sort(sort_list, 0, len(sort_list))))
    print("Heap sort: {}".format(np.array(heap_sort(list(sort_list)))))
    print("Heap Descend sort: {}".format(np.array(heap_sort_descend(list(sort_list)))))
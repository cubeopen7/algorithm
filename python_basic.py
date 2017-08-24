# -*- coding: utf-8 -*-

def return_int(a):
    a += 1

def return_list(some_list):
    some_list.append(1)

def test_str(a):
    a += "b"

if __name__ == "__main__":
    t = 1
    return_int(t)
    print(t)
    t2 = [2]
    return_list(t2)
    print(t2)
    t3 = "a"
    test_str(t3)
    print(t3)
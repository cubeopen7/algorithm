# -*- coding: utf-8 -*-

import random
import numpy as np


class UnionFind(object):
    # With Quick-union, Weighting, and Path compression

    def __init__(self, N):
        self.id = np.arange(N, dtype=np.int64)
        self.sz = np.ones(N, dtype=np.int64)
        a = 1

    def root(self, x):
        while x != self.id[x]:
            self.id[x] = self.id[self.id[x]]
            x = self.id[x]
        return x

    def find(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        a = self.root(x)
        b = self.root(y)
        if a == b:
            return
        if self.sz[a] <= self.sz[b]:
            self.id[a] = b
            self.sz[b] += self.sz[a]
        else:
            self.id[b] = a
            self.sz[a] += self.sz[b]


class Percolation(object):
    def __init__(self, N):
        self.N = N
        self.num = N ** 2
        self.blocks = np.zeros(self.num, dtype=np.int64)
        self.uf = None

    def restart(self):
        self.blocks = np.zeros(self.num, dtype=np.int64)
        new_uf = UnionFind(self.num + 2)
        for i in np.arange(self.N):
            new_uf.union(i, self.num)
        for i in np.arange(self.num)[-self.N:]:
            new_uf.union(i, self.num + 1)
        return new_uf


    def is_linked(self):
        return self.uf.find(self.num, self.num + 1)

    def blocked(self, x):
        return self.blocks[x] == 0

    def notblocked(self, x):
        return self.blocks[x] != 0

    def available(self, x):
        ava_list = []
        for i in [x + 1, x - 1, x - self.N, x + self.N]:
            if i < 0 or i >= self.num:
                continue
            if self.notblocked(i):
                ava_list.append(i)
        return ava_list

    def start(self):
        self.uf = self.restart()
        random_list = random.sample(range(self.num), self.num)
        i = 0
        while ~self.is_linked():
            k = random_list[i]
            i += 1
            self.blocks[k] = 1
            for index in self.available(k):
                self.uf.union(k, index)
        return self.blocks.sum() / self.num

    def experiment(self, times=100000):
        result = []
        for _ in range(times):
            result.append(self.start())
        return np.mean(result)


if __name__ == "__main__":
    import time
    exp_time = 100000
    toc = time.time()
    p = Percolation(5).experiment(times=exp_time)
    time_consume = time.time() - toc
    print("Complete {} times experiment, costing {}s, resulting the p is {}.".format(exp_time, time_consume, p))
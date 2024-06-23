# -*- coding: utf-8 -*-
from itertools import combinations


def all_variants(txt):
    for i in range(1, len(txt) + 1):
        for str1 in combinations(txt, i):
            yield ''.join(list(str1))


text = 'abc'  # Из задания
for variant1 in all_variants(text):
    print(variant1)

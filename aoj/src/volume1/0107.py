# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0107
import pprint, sys, time, itertools, math, cmath, re, datetime, copy, collections, calendar

import numpy as np
import pandas as pd

from sympy import isprime, primefactors, Symbol, integrate, nextprime, sieve, prime, primerange, Polygon, Point
from numpy import linalg as LA

print(sys.version)
const_m, const_M = [pow(2, f) for f in [-10, 10]]
f_eps = 10**-4

def ret_f_length_diagonal(f_x, f_y):
    return (f_x**2 + f_y**2)**0.5

assert ret_f_length_diagonal(3, 4) == 5

# https://docs.python.org/ja/3/library/itertools.html
def main(arg, libed=False, n=3):
    ret = []

    fs_size_wk, fs_radius_r = arg
    if libed:
        ret = [2*r > min([
            ret_f_length_diagonal(f_x, f_y) for f_x, f_y in itertools.combinations(fs_size_wk, 2)
        ]) for r in fs_radius_r]
    else:
        f_min_length_diagonal = min([
            ret_f_length_diagonal(f_x, f_y) for f_x, f_y in itertools.combinations(fs_size_wk, 2)
        ])
        ret = [2*r > f_min_length_diagonal for r in fs_radius_r]
    
    return ret

def app(*args, n=3, l_max=1000):
    ret = []
    for arg in args:
        s = []
        for libed in [True, False]:
            ep = []
            for i in range(n):
                st = time.time()
                try:
                    r = main(arg, libed=libed)
                except Exception as e:
                    r = e
                except TimeoutError as e:
                    r = e
                ep = ep + [time.time() - st]
            s.append([libed, round(np.mean(ep[1:]), 9), str(r)[:l_max]])
        ret.append([str(arg)[:l_max], s])
        
    assert type(ret) == list
    return ret

### spec
# input: fs_size_wk, fs_radius_r
# output: i_deg_through
pprint.pprint(app(
    # basic examples
    [
        [10, 6, 8],
        [4, 8, 6, 2, 5],
    ],
    # border examples
    [
        [0, 0, 0],
        [],
    ],
    # additional examples
    # exceptional examples
    "例外入力",
))

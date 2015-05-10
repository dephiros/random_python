#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def double_to_bin_less_than_1(d):
    if d > 1 or d < 0: return "ERROR"
    elif d == 1: return "1."
    result = "0."
    while(d > 0):
        if len(result) - 2 >= 32: return "ERROR"
        d = d << 1
        if d >= 1:
            result += '1'
            d -= 1
        else:
            result += '0'
    return result

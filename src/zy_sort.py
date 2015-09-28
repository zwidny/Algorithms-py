# -*- coding: utf-8 -*-


def quick_sort(s):
    """Quick sort.
    Args:
      s - must support len()
    Return:
      type(s) - sorted s, from min to max.

    Todo:
      remove len() support
    """
    if len(s) < 2:
        return s
    p = s.pop()
    pl = list(filter(lambda x: x < p, s))
    pg = list(filter(lambda x: x > p, s))
    pl = quick_sort(pl)
    pg = quick_sort(pg)
    return pl + [p] + pg


def merge(s):
    '''sorted s based on merging algorithm

    Args:
      s - a list or tuple that supports len function and slice

    Return:

    '''
    def merge_func(s1, s2):
        s_l = len(s1) + len(s2)
        i = j = 0
        s_n = [0] * s_l
        while i + j < s_l:
            if i < len(s1) and j < len(s2):
                if s1[i] < s2[j]:
                    s_n[i+j] = s1[i]
                    i += 1
                else:
                    s_n[i+j] = s2[j]
                    j += 1
            elif not i < len(s1):
                s_n[i+j] = s2[j]
                j += 1
            elif not j < len(s2):
                s_n[i+j] = s1[i]
                i += 1
        return s_n

    if len(s) < 2:
        return s
    mid = len(s) // 2
    return merge_func(s[:mid], s[mid:])

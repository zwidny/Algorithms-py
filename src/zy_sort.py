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
    pl = type(s)(filter(lambda x: x < p, s))
    pg = type(s)(filter(lambda x: x > p, s))
    pl = quick_sort(pl)
    pg = quick_sort(pg)
    return pl + [p] + pg

def get_palindrome_length(s, index):
    """
    Returns length of longest palindromic substring centered in the given index.
    """
    length = 1
    while index + length < len(s) and index - length >= 0:
        if s[index + length] == s[index - length]:
            length += 1
        else:
            break

    return length - 1


def interleave(s):
    """
    Returns a interleaved version of a given string. 'aaa' --> '#a#a#a#'.
    Thanks to this function we don't have to deal with even/odd palindrome
    length problem.
    """
    ret = []
    for s in s:
        ret.extend(['#', s])
    ret.append('#')

    return ''.join(ret)


def manacher(s):
    """
    Computes length of the longest palindromic substring centered on each char
    in the given string. The idea behind this algorithm is to reuse previously
    computed values whenever possible (palindromes are symmetric).

    Example (interleaved string):
    i    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22
    s    #  a  #  b  #  c  #  q  #  q  #  q  #  q  #  q  #  q  #  x  #  y  #
    P    0  1  0  1  0  1  0  1  2  3  4  5  6  5  4  ?
                                    ^        ^        ^        ^
                                  mirror   center   current  right

    We're at index 15 wondering shall we compute (costly) or reuse. The mirror
    value for 15 is 9 (center is in 12). P[mirror] = 3 which means a palindrome
    of length 3 is centered at this index. A palindrome of same length would be
    placed in index 15, if 15 + 3 <= 18 (right border of large palindrome
    centered in 12). This condition is satisfied, so we can reuse value from
    index 9 and avoid costly computation.
    """
    right = 0
    center = 0
    s = interleave(s)
    p = [_ for _ in range(len(s))]

    for i in range(1, len(s)):
        mirror = 2 * center - i
        if i + p[mirror] <= right and mirror >= len(s) - i:
            p[i] = p[mirror]
        else:
            plen = get_palindrome_length(s, i)
            p[i] = plen
            if plen > 1:
                center = int(i)
                right = center + plen

    return [e // 2 for e in p]


def get_palindrome_number(s):
    return sum(manacher(s))


def get_longest_palindrome(s):
    cm = manacher(s)
    center = cm.index(max(cm)) // 2
    conditional = 1 if center % 2 == 1 else 0
    s_idx = cm.index(max(cm))
    radius = int(cm[s_idx])
    return s[center-radius:center+radius+conditional]

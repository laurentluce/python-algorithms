def string_matching_naive(text='', pattern=''):
    """Returns positions where pattern is found in text.

    We slide the string to match 'pattern' over the text

    O((n-m)m)
    Example: text = 'ababbababa', pattern = 'aba'
                     string_matching_naive(t, s) returns [0, 5, 7]
    @param text text to search inside
    @param pattern string to search for
    @return list containing offsets (shifts) where pattern is found inside text
    """

    n = len(text)
    m = len(pattern)
    offsets = []
    for i in range(n-m+1):
        if pattern == text[i:i+m]:
            offsets.append(i)

    return offsets


def string_matching_rabin_karp(text='', pattern='', hash_base=256):
    """Returns positions where pattern is found in text.

    worst case: O(nm)
    O(n+m) if the number of valid matches is small and the pattern is large.

    Performance: ord() is slow so we shouldn't use it here

    Example: text = 'ababbababa', pattern = 'aba'
             string_matching_rabin_karp(text, pattern) returns [0, 5, 7]
    @param text text to search inside
    @param pattern string to search for
    @param hash_base base to calculate the hash value
    @return list containing offsets (shifts) where pattern is found inside text
    """

    n = len(text)
    m = len(pattern)
    offsets = []
    htext = hash_value(text[:m], hash_base)
    hpattern = hash_value(pattern, hash_base)
    for i in range(n-m+1):
        if htext == hpattern:
            if text[i:i+m] == pattern:
                offsets.append(i)
        if i < n-m:
            htext = (hash_base *
                     (htext -
                      (ord(text[i]) *
                       (hash_base ** (m-1))))) + ord(text[i+m])

    return offsets


def hash_value(s, base):
    """Calculate the hash value of a string using base.

    Example: 'abc' = 97 x base^2 + 98 x base^1 + 99 x base^0
    @param s string to compute hash value for
    @param base base to use to compute hash value
    @return hash value
    """
    v = 0
    p = len(s)-1
    for i in range(p+1):
        v += ord(s[i]) * (base ** p)
        p -= 1

    return v


def string_matching_knuth_morris_pratt(text='', pattern=''):
    """Returns positions where pattern is found in text.

    O(m+n)
    Example: text = 'ababbababa', pattern = 'aba'
        string_matching_knuth_morris_pratt(text, pattern) returns [0, 5, 7]
    @param text text to search inside
    @param pattern string to search for
    @return list containing offsets (shifts) where pattern is found inside text
    """
    n = len(text)
    m = len(pattern)
    offsets = []
    pi = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == m:
            offsets.append(i - m + 1)
            q = pi[q-1]

    return offsets


def compute_prefix_function(p):
    m = len(p)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = pi[k - 1]
        if p[k] == p[q]:
            k = k + 1
        pi[q] = k
    return pi


def string_matching_boyer_moore_horspool(text='', pattern=''):
    """Returns positions where pattern is found in text.

    O(n)
    Performance: ord() is slow so we shouldn't use it here

    Example: text = 'ababbababa', pattern = 'aba'
         string_matching_boyer_moore_horspool(text, pattern) returns [0, 5, 7]
    @param text text to search inside
    @param pattern string to search for
    @return list containing offsets (shifts) where pattern is found inside text
    """
    m = len(pattern)
    n = len(text)
    offsets = []
    if m > n:
        return offsets
    skip = []
    for k in range(256):
        skip.append(m)
    for k in range(m-1):
        skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            offsets.append(i + 1)
        k += skip[ord(text[k])]

    return offsets


def atoi(s):
    """Convert string to integer without doing int(s).

    '123' -> 123
    @param s string to convert.
    @returns integer
    """
    if not s:
        raise ValueError
    i = 0
    idx = 0
    neg = False
    if s[0] == '-':
        neg = True
        idx += 1

    for c in s[idx:]:
        i *= 10
        i += int(c)

    if neg:
        i = -i

    return i


def reverse_string_words(s):
    """Reverse words inside a string (in place).

    Since strings are immutable in Python, we copy the string chars to a list
    first.
    'word1 word2 word3' -> 'word3 word2 word1'

    Complexity: O(n)

    @param s string words to reverse.
    @returns reversed string words.
    """
    def reverse(l, i, j):
        # 'word1' -> '1drow'
        # Complexity: O(n/2)
        while i != j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1

    w = [e for e in s]
    i = 0
    j = len(w) - 1
    reverse(w, i, j)

    i = 0
    j = 0
    while j < len(w):
        while j < len(w) and w[j] != ' ':
            j += 1
        reverse(w, i, j-1)
        i = j + 1
        j += 1

    return ''.join(e for e in w)


def rabin_karp_matcher(text, pattern, d, q):
    """
    Rabin-Karp string matcher.

    :param text:
    :type text: str
    :param pattern:
    :type pattern: str
    :param d: The length of the alphabet of text
    :type d: int
    :param q: A prime number
    :type q: int
    :return:
    """
    n = len(text)
    m = len(pattern)
    h = d**(m - 1) % q
    p = 0
    t = 0

    for i in range(0, m):   # preprocessing:
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    print('\nRabin-Karp string matcher:\n')

    for s in range(0, n - m):   # matching:
        text_slice = text[s:s + m]
        are_the_same_string = pattern == text_slice
        print('"%s" is "%s"? %r' % (text_slice, pattern, are_the_same_string))

        if p == t and are_the_same_string:
            print('Pattern found with shift %d' % s)

        if s < n - m:
            t = (d*(t - ord(text[s])*h) + ord(text[s + m])) % q

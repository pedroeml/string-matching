
def naive_string_matcher(text, pattern):
    """
    Naive string matcher.

    :param text:
    :type text: str
    :param pattern:
    :type pattern: str
    """
    n = len(text)
    m = len(pattern)

    print('\nNaive string matcher:\n')

    for s in range(0, n - m):   # preprocessing:
        text_slice = text[s:s + m]
        are_the_same_string = pattern == text_slice
        print('"%s" is "%s"? %r' % (text_slice, pattern, are_the_same_string))
        if are_the_same_string:
            print('Pattern found with shift %d' % s)

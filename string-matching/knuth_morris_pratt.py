
def kmp_matcher(text, pattern):
    """
    Knuth-Morris-Pratt string matcher.

    :param text:
    :type text: str
    :param pattern:
    :type pattern: str
    :return:
    """
    n = len(text)
    m = len(pattern)
    prefixes = compute_prefix_function(pattern)
    q = 0

    print('\nKnuth-Morris-Pratt string matcher:\n')

    for i in range(1, n + 1):
        while q > 0 and pattern[q] != text[i - 1]:
            q = prefixes[q - 1]

        is_the_same_char = pattern[q] == text[i - 1]
        print('"%s" is "%s"? %r' % (text[i - 1], pattern[q], is_the_same_char))

        if is_the_same_char:
            q += 1

        if q == m:
            print('Pattern found with shift %d' % (i - m))
            q = prefixes[q - 1]


def compute_prefix_function(pattern):
    """
    Computes the prefix array for KMP.

    :param pattern:
    :type pattern: str
    :return:
    """
    m = len(pattern)
    prefixes = [0]*(m+1)
    i = 0
    
    for q in range(2, m + 1):
        while i > 0 and pattern[i] != pattern[q - 1]:
            i = prefixes[i]
        
        if pattern[i] == pattern[q - 1]:
            i += 1
        
        prefixes[q] = i
    
    return prefixes[1:]


def test_kmp():
    print(compute_prefix_function('ATAG'))      # expects [0, 0, 1, 0]
    print(compute_prefix_function('AGTC'))      # expects [0, 0, 0, 0]
    print(compute_prefix_function('ACACAGT'))   # expects [0, 0, 1, 2, 3, 0, 0]

    kmp_matcher('ACATACGACACAGT', 'ACACAGT')    # expects shift of 7

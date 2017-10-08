import random
import sympy
from naive import naive_string_matcher
from rabin_karp import rabin_karp_matcher
from knuth_morris_pratt import kmp_matcher


text = 'ABABCDABCAAABACCABCDD'
pattern = 'ABCD'
alphabet = set(text)    # the alphabet contains the same characters present in the text
d = len(alphabet)
primes = [i for i in range(1, 1000) if sympy.isprime(i)]
q = random.choice(primes)

naive_string_matcher(text, pattern)
rabin_karp_matcher(text, pattern, d, q)
kmp_matcher(text, pattern)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s = input().split()

for i in list(combinations_with_replacement(sorted(s[0]),int(s[1]))):
    print(''.join(i))
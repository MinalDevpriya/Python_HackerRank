#https://www.hackerrank.com/challenges/validate-a-roman-number/problem
regex_pattern = r"^((?P<a>[IVXCDM])(?!(?P=a){3})|(?P<l>L)(?!(?P=l)))+$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
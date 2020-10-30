import re
regex_pattern = r'[.,]'
print re.search(regex_pattern,raw_input())
print("\n".join(re.split(regex_pattern, raw_input())))
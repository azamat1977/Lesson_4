import re

line = 'asdf fjdk;afed, fjek, asdf, foo'

#result = re.split(r'[;,\s]', line)
result = re.sub(r'[;,\s]', ' ', line)

print(result)
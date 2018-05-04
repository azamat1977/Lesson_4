import re

#result = re.findall(r'\w+', 'AV is largest Analytics community of India')
#result = re.findall(r'\b[aA]\w+', 'AV is largest Analytics community of India')
#result = re.findall(r'\b[^aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
result = re.findall(r'\b[^aeiouAEIOU ]\w+', 'AV is largest Analytics community of India')

print(result)
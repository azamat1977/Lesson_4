import re

result = re.findall(r'\w+\s(\w+)\s(\w+)', str)

response = urlopen('file:///home/azamat/PycharmProjects/Lesson_4/index.html')
html = response.read()

print(result)
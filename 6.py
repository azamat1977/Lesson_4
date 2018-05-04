import re

li = ['9999999999','999999-999','99999x9999']


for val in li:

    if re.match (r'[5-9]{1}[0-9]{9}', val) and len(val) == 10:

        print('yes')

else:

        print('no')


import re

email = 'jose@tecladocode.com'
expression = '[a-z\.]+'

matches = re.search(expression, email)


print(matches.group(0))
print(matches.group(1))
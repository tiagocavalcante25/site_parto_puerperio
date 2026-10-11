import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ids = re.findall(r'id=["\']([^"\']+)["\']', html)
print('Total IDs:', len(ids))
for i in ids:
    if any(k in i.lower() for k in ['modulo', 'calc', 'simulador', 'flashcard', 'quiz', 'distocia', 'high-yield', 'nav', 'theme', 'drawer', 'partograph']):
        print('  ID:', i)

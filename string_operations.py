
actor = "Chris Hemsworth"
print(len(actor))
print(type(actor))

print(actor.upper())
a = actor.lower()
print(a)

print(actor.count('h'))
print(actor.count('H'))
actor2 = actor.lower()
print(actor2.count('h'))
print(actor.lower().count('h'))

x = "     FOOBAR    "
y = x.lower().strip()
print(x)
print(y)

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))

print("wor" in actor)
print("piece" in actor)

target = 'worth'
pos = actor.find(target)
result = actor[pos:pos + len(target)]
print(result)

print(actor.find('value'))

s = "           able was I ere I saw Elba      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "blbbbbblllbbbllblbable was I ere I saw Elbalbbblllblbllblbllblblbbbllllll"
print("|" + s.lstrip("bl") + "|")
print("|" + s.rstrip("bl") + "|")
print("|" + s.strip("bl") + "|")
print()

print(actor)
print(actor.replace('Chris', 'Liam'))

values = ['a', 'b', 'c', 'd']

print(','.join(values))
print(' '.join(values))
print(''.join(values))
print(' / '.join(values))




import unicodedata


def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value={}, name={}, value2={}'.format(value, name, value2))


unicode_test('A')
unicode_test('\u00a2')

print(unicodedata.name('\u00e9'))

unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')

place = 'caf\u00e9'

u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'

print(len('\U0001f47b'))

snowman = '\u2603'
print(len(snowman))
ds = snowman.encode('utf-8')
print(ds, len(ds))
print(snowman.encode('ascii', 'ignore'))
print(snowman.encode('ascii', 'replace'))
print(snowman.encode('ascii', 'backslashreplace'))

print(type(place))
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
place2 = place_bytes.decode('utf-8')
# place3=place_bytes.decode('ascii')

print('%s' % 42, '%d' % 42, '%x' % 42, '%o' % 42, '%s' %
      7.03, '%f' % 7.03, '%e' % 7.03, '%g' % 7.03, '%d%%' % 100,)
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("Our cat %s weighs %s pounds" % (cat, weight))

n, f, s = (42, 7.03, 'string cheese')
print('%d %f %s' % (n, f, s))
print('%10d %10f %10s' % (n, f, s))
print('%-10d %-10f %-10s' % (n, f, s))
print('%10.4d %10.4f %10.4s' % (n, f, s))
print('%.4d %.4f %.4s' % (n, f, s))
print('%*.*d' % (10, 4, n))

print('{} {} {}'.format(n, f, s))
print('{2} {0} {1}'.format(f, s, n))
print('{n} {f} {s}'.format(n=42, f=7.03, s='string cheese'))
d = {'n': 42, 'f': 7.03, 's': 'string cheese'}
print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))
print('{0:10d} {1:10f} {2:10s}'.format(n, f, s))
print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))
print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))
print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))
print('{0:!^20s}'.format('BIG SALE'))

import re
result1 = re.match('You', 'Young Frankenstein')
youpattern = re.compile('You')
result2 = youpattern.match('Young Frankenstein')

source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())
m = re.match('Frank', source)
print(m)

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.match('.*Frank', source)
if m:
    print(m.group())

m = re.findall('n', source)
print(m)

m = re.findall('n.', source)
print(m)

m = re.findall('n.?', source)
print(m)

m = re.split('n', source)
print(m)

m = re.sub('n', '?', source)
print(m)

import string
printable = string.printable
print(len(printable))
print(printable)

print(re.findall('\d', printable))
print(re.findall('\w', printable))
print(re.findall('\s', printable))

source1 = '''I wish I may, I wish I might
Have a dish of fish tonight.'''
print(re.findall('^wish', source1))
print(re.findall('fish tonight\.$', source1))
print(re.findall('[wf]ish', source1))
print(re.findall('[wsh]+', source1))
print(re.findall('ght\W', source1))
print(re.findall('I (?=wish)', source1))
print(re.findall('(?<=I) wish', source1))
print(re.findall(r'\bfish', source1))
m = re.search(r'(. dish\b).*(\bfish)', source1)
print(m.group())
print(m.groups())
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source1)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
the_byte_array = bytearray(blist)
print(the_byte_array)

the_byte_array[1] = 127
print(the_byte_array)
bytelist = bytes(range(256))
print(bytelist)

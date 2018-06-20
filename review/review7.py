import unicodedata
mistery='\U0001f4a9'
print(unicodedata.name(mistery))

pop_bytes=mistery.encode('utf-8')
print(pop_bytes)

pop_string=pop_bytes.decode('utf-8')

print("My kitty cat likes %s,\
My kitty cat likes %s,\
My kitty cat fell on his %s\
And now thinks he's a %s" %('roast beef','ham','head','clam'))

letter='''Dear {salutation} {name},\n\
Thank you fou your letter. We are sorry that our {product}\
 {verbed} in your {room}. Please note that it should never be used\
 in a {room}, especially near any {animals}.\
  Send us your'''

response={'salutation':'my friend', 'name':'name1','product':'GC'\
, 'verbed':'controler', 'room':'408', 'animals':'bears'}
print(letter)
print(letter.format(**response))

mammoth='''We have seen thee, queen of cheese,
    Lying quietly at your ease,
    Gently fanned by evening breeze,
    Thy fair form no flies dare seize.

    All gaily dressed soon you'll go
    To the great Provincial show,
    To be admired by many a beau
    In the city of Toronto.

    Cows numerous as a swarm of bees,
    Or as the leaves upon the trees,
    It did require to make thee please,
    And stand unrivalled, queen of cheese.

    May you not receive a scar as
    We have heard that Mr. Harris
    Intends to send you off as far as
    The great world's show at Paris.

    Of the youth beware of these,
    For some of them might rudely squeeze
    And bite your cheek, then songs or glees
    We could not sing, oh! queen of cheese.

    We'rt thou suspended from balloon,
    You'd cast a shade even at noon,
    Folks would think it was the moon
    About to fall and crush them soon.'''

import re
print(re.findall(r'\bc\w*\b',mammoth))
print(re.findall(r'\bc\w{3}\b',mammoth))
print(re.findall(r'\b\w*r\b',mammoth))
print(re.findall(r'\b\w*l\b',mammoth))
print(re.findall(r'\b\w*[aiueo]{3}[^aiueo\s]*\w*\b',mammoth))

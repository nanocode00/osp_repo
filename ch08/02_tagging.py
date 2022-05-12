from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()
mystr = u'아버지가방에들어가신다.'
pprint(kkma.pos(mystr))


mystr = u'아버지가 방에 들어가신다.'
pprint(kkma.pos(mystr))

from konlpy.tag import Twitter
twitter = Twitter()
mystr = u'아버지가방에들어가신다.'
pprint(twitter.pos(mystr))

mystr = u'아버지가 방에 들어가신다.'
pprint(twitter.pos(mystr))
#!/usr/bin/python2
import re



###
# CHECKING FOR A PAIR
# http://docs.python.org/2/library/re.html#checking-for-a-pair
###
def displaymatch(match):
    if match is None:
        print ('None')
        return
    dm ='<Match: %r, groups=%r>' % (match.group(), match.groups())
    print (dm)
    return


"""
Suppose you are writing a poker program where a player's hand is 
represented as a 5-character string with each character representing 
a card, "a" for ace, "k" for king, "q" for queen, "j" for jack, "t" for 10, 
and "2" through "9" representing the card with that value.

To see if a given string is a valid hand, one could do the following:
"""
valid = re.compile(r"^[a2-9tjqk]{5}$")

displaymatch(valid.match("akt5q"))  # Valid.
displaymatch(valid.match("akt5e"))  # Invalid.
displaymatch(valid.match("akt"))    # Invalid.
displaymatch(valid.match("727ak"))  # Valid.


"""
That last hand, "727ak", contained a pair, or two of the same valued cards.
To match this with a regular expression, one could use backreferences as 
such:
"""
pair = re.compile(r".*(.).*\1")

displaymatch(pair.match("717ak"))     # Pair of 7s.
displaymatch(pair.match("718ak"))     # No pairs.
displaymatch(pair.match("354aa"))     # Pair of aces.


"""
To find out what card the pair consists of, one could use the group() method 
of MatchObject in the following manner:
"""
ppm1 = pair.match("717ak").group(1)
print =(ppm1)
#print pair.match("718ak").group(1)  # No pairs.
ppm2 = pair.match("354aa").group(1)
print =(ppm2)



###
# SIMULATING SCANF()
# http://docs.python.org/2/library/re.html#simulating-scanf
###

string = '/usr/sbin/sendmail - 0 errors, 4 warnings'
valid = re.compile(r"(\S+) - (\d+) errors, (\d+) warnings")

pvm1 = valid.match(string).groups()
print =(pvm1)


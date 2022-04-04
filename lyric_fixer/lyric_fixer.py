dsb = """Just a small town girl
Livin' in a lonely world
She took the midnight train goin' anywhere
Just a city boy
Born and raised in South Detroit
He took the midnight train goin' anywhere
A singer in a smokey room
The smell of wine and cheap perfume
For a smile they can share the night
It goes on and on, and on, and on
Strangers waiting
Up and down the boulevard
Their shadows searching in the night
Streetlights people
Livin' just to find emotion
Hidin' somewhere in the night
Workin' hard to get my fill
Everybody wants a thrill
Payin' anything to roll the dice just one more time
Some will win, some will lose
Some were born to sing the blues
Oh, the movie never ends
It goes on and on, and on, and on
Strangers waiting
Up and down the boulevard
Their shadows searching in the night
Streetlights people
Livin' just to find emotion
Hidin' somewhere in the night
Don't stop believin'
Hold on to that feelin'
Streetlight people
Don't stop believin'
Hold on
Streetlight people
Don't stop believin'
Hold on to that feelin'
Streetlight people"""

dsbWords = dsb.replace('\n', ' ').split(' ')

print("Don't Stop Believin' is " + str(len(dsbWords)) + " words long.")

# A set is like a list, but with no duplicate entries. 
# Turning a list into a set is a handy way to remove duplicates.
print("But it only has " + str(len(set(dsbWords))) + " unique words.")

bad_singing = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""

def fix_lyrics(bad_version):
  splitted = bad_version.replace('\n', '').split(' ')
  print(splitted)
  

fix_lyrics(bad_singing)
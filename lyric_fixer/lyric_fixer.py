# lyric fixer 1.0
# If you don't remember the correctness of your favorite song,
# this code search the correct spelling by comparing the closet correct word around your version of the music.
# 

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

dsbWords = dsb.split(' ')

bad_singing = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""

def fix_lyrics(bad_version):
  splitted = bad_version.split(' ') # transform in a array
 
  for index in range(len(splitted)):
    if not splitted[index] in dsbWords:
      splitted[index] = find_correct_word(index, splitted, dsbWords)
  splitted = list(filter(None, splitted))
  print(splitted)

def find_correct_word(index, wrong_array, correct_array):
  aperture = 1
  next_word_is_incorrect = True
  while next_word_is_incorrect: # defines the size of the neighbor copmarison in aperture
    if wrong_array[index + aperture] in correct_array:
      next_word_is_incorrect = False
    else:
      aperture += 1
  
  for idx in range (0, len(correct_array)): # find the correct answer in a tweezer movement
    if correct_array[idx] == wrong_array[index - 1] and correct_array[idx + 1 + aperture] == wrong_array[index + aperture]:
      return correct_array[idx + 1]

# def music_printer(music_array):
#   for index in range(0, len(music_array)-1):
#     if is_capitalized(music_array[index + 1]):
#       if is_phrase_ending(index, music_array)
#       print("#"+music_array[index],sep = "\n")
#     else:
#       print(music_array[index], end=" ")

# def is_capitalized(word):
#   capital = word.capitalize()
#   if (capital.__eq__(word)):
#     return True
#   else:
#     return  
    


fix_lyrics(bad_singing) # Here where all begins
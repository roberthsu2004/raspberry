def edit_story(words, func):
    for word in words:
        print(func(word))
        
#stairs = ['thud', 'meow', 'thud', 'hiss']

#def enliven(word):
#   return word.capitalize() + '!'


#edit_story(stairs,enliven)

edit_story(['thud', 'meow', 'thud', 'hiss'],lambda word : word.capitalize()+'!')

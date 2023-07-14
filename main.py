import askai as ai
sentence = 'Hi, I am EmotiBot. Lets talk!'
print(sentence)

# The line below asks the user to provide an input
name = input('What would you like to be called?\n')

# The line below asks the user to provide an input
print('Nice to meet you ', name)
age = input('How old are you?\n')
print('Wow, ',age, ' is a great age' )
print('Lets talk some more')



# Ask the user to enter their feeliing
mood_input = input('How are you feeling today?')


# Below is where code asks AI weather the sentence is a sad or a happy feeling
mood = ai.get_prediction(mood_input)

# Different code is executed depending on weather mood is happy or sad
if mood == 'happy':
    print('I am so glad to hear that!')
elif mood == 'sad':
  # if someone is sad 
    print('I am so sorry you feel that way, lets talk some more!')
    game_condition = input('Do you like to play games, say yes or no\n')
    if game_condition=='yes':
       print('Please play a game and see if you feel better!!')
    else:
       print('Perhaps there is something else that you like to do!')
else:
    print('Sorry, I dont understand, can you tell me more?')
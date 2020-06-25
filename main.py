from random import randint

# myfunc adds one to the argument
def myfunc(an_arg):
  '''more info here'''
  return an_arg + 1
  
def continue_function (continue_answer):
  if continue_answer == "yes":
    return True
  else:
    return False


# Open a very big file of words 
words = open("words.txt")

# Search the file for words with 8 characters
# Exclude words with an upper case initial letter
candidates = []
for word in words:
  word = word.strip()
  if len(word) == 8 and word[0].islower():
    candidates.append(word)

print("======================================== \nWELCOME TO THE SUPER EASY ANAGRAM GAME \n---------------------------------------- ")


print()

# Select one of the candidate words at random
choice_num = randint(0,len(candidates)-1)

print("Random 8 letter word")

# print("Actual answer", candidates[choice_num].lower())
# Scramble the word, by sorting the letters in 
# alphabetic order.
unscrambled = candidates[choice_num].lower()
scrambled = sorted(unscrambled)

#print(unscrambled)
print("["+"] [".join(scrambled)+"]")
print()

user_answer = input("What do you think the correct word is? \n")

print()


#  if user_answer != word:
#   continue_function()

if user_answer == unscrambled:
  print("You are one smart mofo, you are correct!")
else:
  print("That is incorrect. \nDon't beat yourself up, this is ridiculously difficult.")
  print()
  continue_answer= input("Do you want to try again? yes or no \n")
  print()
  while continue_function(continue_answer) == True: 
    print()
    user_answer = input("What do you think the correct word is? \n")
    if user_answer == unscrambled:
      print("You are one smart mofo, you are correct!")
      break
    else:
       print("That is incorrect. \nDon't beat yourself up, this is ridiculously difficult.")
       print()
       continue_answer= input("Do you want to try again? yes or no \n")
       print()
  if continue_function(continue_answer) == False:
    command = input("Would you like to reveal the answer? yes or no \n")
    print()
    if command=='yes':
      print(candidates[choice_num].lower(), "...obviously.")
    else:
      print('Fine be like that...')
# continue_answer= input("Do you want to try again? yes or no \n")


     
print()


  # continue_answer= input("Do you want to try again? yes or no \n")

# How to use while::

# answer_correct = False
# while answer_correct == False:

#   if user_answer == word:
#     answer_correct = True

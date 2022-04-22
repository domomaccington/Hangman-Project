import random

Words =["houston,""brooklyn","capture","wireless","mobile","charging","manhatten","trenton","screaming","macbookpro"]

secretword =random.choice(Words)

#Dominick

attempts = 10

guesses = []

done = False

while not done:
    for letter in secretword:
        if letter.lower() in guesses:
            print (letter,end="")
        
        else:
             print ("_", end=" ")     
    
    print (" ")                
      
    guess = input(f"attempts left { attempts} another guess: ")
    guesses.append( guess.lower())
    if guess.lower ()not in secretword. lower ():
        attempts -= 1
        if attempts == 0:
            break
       
    done = True 
    for letter in secretword:
        if letter. lower () not in guesses:
            done = False

if done:
    print(f"You got it! it was {secretword}!")
    
else: 
    print (f"game over you lost! The word was {secretword}!")

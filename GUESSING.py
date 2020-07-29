#import tkinter module
from tkinter import *

#import other necessary modules
import random as rand

#creating root object
root=Tk()

#defining size of window
root.geometry("700x400")

#setting up the title window
root.title("Guessing Game")

Tops=Frame(root,width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)

f1.pack(side=TOP)

#welcome
label=Label(Tops,font=('helvetica',40,'bold'),
              text="The Guessing Game",
                fg='Brown',bd=10,anchor='w')

label.grid(row=0,column=0)


lblInfo=Label(Tops,font=('arial',20,'bold'),
              text="Welcome",fg="Steel Blue",bd=10,anchor='w')

lblInfo.grid(row=1,column=0)

#exit function
def qExit():
    root.destroy()

#reference
lblReference=Label(f1,font=('arial',16,'bold',),text="NAME:",bd=16,anchor="w")
lblReference.grid(row=3,column=1)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="green",justify='left')
txtReference.grid(row=3,column=2)

#guessing number
def gnum():
    print('                         GUESSING NUMBER')
    name = txtReference.get()
    number = rand.randint(1,200)

    number_of_guesses = 0
    print('okay! '+ name+ ' I am Guessing a number between 1 and 200:')

    print("Clues:")

    m=0
    for i in range(2,number):
        if(number%i==0):
            print("Number is not a prime")
            break
    
    if(number==1):
        print("Number divides every number")

    for j in range(1,number):
        if(number%j==0):
            m+=1
        else:
            m+=0

    if(m==1):
        print("Number is prime")
    

    if(number%2==0):
        print('Number is even')
    if(number%3==0):
        print('Number is divisible by 3')
    if(number%5==0):
        print('Number is divisible by 5')
    if(number%7==0):
        print('Number is divisible by 7')


    while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            break
    if guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('You did not guess the number, The number was ' + str(number))

    input("\n\nPress Enter to exit")

    print(' ')
    print(' ')




    

#guessing name
def gname():
    print('                         GUESSING CITY NAME')
    name = txtReference.get() 
    print("Good Luck ! ", name)

    num = rand.randint(0,22)
    n = rand.randint((2*num),(2*num+1))
    cities = ['srinagar','pulwama','shimla','dharamshala','amritsar',
             'atari','gurugram','chandigarh','haridwar','dehradun',
             'lucknow','agra','pushkar','jaipur','gandhinagar','vadodara',
             'chhindwara', 'bhopal', 'patana','muzaffarpur','ranchi',
             'jamshedpur','kolkata','siliguri','gangtok','namchi','raipur',
             'durg','bhubaneswar','puri','hyderabad','warangal',
             'visakhapatnam','vijaywada','nashik','nagpur','panaji',
             'palolem','bengaluru','mangalore','chennai','kanyakumari',
             'thiruvananthapuram','kochi','dispur','guwahati']
    city = cities[n]

    states = ['JAMMU & KASHMIR','HIMACHAL PRADESH','PUNJAB','HARYANA',
              'UTTARAKHAND','UTTAR PRADESH','RAJASTHAN','GUJARAT',
              'MADHYA PRADESH','BIHAR','JHARKHAND','WEST BANGAL','SIKKIM',
              'CHHATTISGARH','ODISHA','TELANGANA','MAHARASHTA','ANDHRA PRADESH',
              'GOA','KARNATAK','TAMIL NADU','KERALA','ASSAM']
    state = states[num]

    print("Clues")
    print(state)
    print("Guess the characters of city name") 
    guesses = ''  
    turns = 5
  
    while turns > 0: 
        failed = 0

        for char in city:  
            if char in guesses:  
                print(char) 
            else:  
                print("_") 
                failed += 1

        if failed == 0: 
            print("$$$$$$ You Win $$$$$$")  
            print("The city is: ", city, "in", state)  
            break
      
        guess = input("guess a character:")[0]
        guesses += guess  

        if guess not in city: 
            turns -= 1
            print("Wrong") 
            print("You have", + turns, 'more guesses') 
            if turns == 0: 
                print("###### You Loose ######")

    input("\n\nPress Enter to exit")

    print(' ')
    print(' ')

   



    
    

#jumbled word
def jw():
    name = txtReference.get()
    print('Okay!  '+ name + '  Lets Play')
    
    #The Word Jumble
    #The computer picks a random word and then "jumbles" it
    #The player has to guess the original word


    n = rand.randint(0,14)
    turn = 5


    #create a sequence of words to choose from
    words = ("sachin","dhoni",
            "gandhi","messi","ronaldo","sania","saina","modi","darwin",
            "obama","newton","ramanujan","einstein","hawking","tolstoy")

    #The Hints

    hints =("God of Cricket","Captain Cool","father of nation","famous footballer",
            "famous footballer","famous Indian tennis player","famous Indian badminton player",
            "Current Indian PM","Theorey of evolution","44th President of the USA ",
            "father of calculus", "After India's National Mathematics Day is Celebrated",
            "Theorey of relativity","A brief history of Time"," Author of war and peace" )

    #pick one word randomly from the sequence

    word = words[n]
    #Order that connects  hints to the words 



    hint = hints[n]

    
    #create a variable to use later to see if the guess is correct
    correct=word

    #create a jumbled version of the word
    jumble=""
    while word:
        position=rand.randrange(len(word))
        jumble+=word[position]
        word=word[:position]+word[(position+1):]

    #start the game
    print(
        """
                     Welcome to The WORD JUMBLE!


                Unscramble the letters to make a word.
                            GOOD LUCK!





    """
    )

    print("The jumble is: ", jumble)
    print ("THE HINT: ",hint)



    #Guessing mechanism
    guess=input("\nYour guess: ")

    
    for turns in range(1,4):
    
        while guess!=correct and guess!="":
            guess=input("Your guess: ")


    #Correct anwser     
    if guess==correct:
    
        print("That's it! You guessed it.\n")
    



    input("\n\nPress Enter to exit")

    print(' ')
    print(' ')
    
#guessing number button
btngnum=Button(f1, padx=16,pady=8,bd=16,fg="black",font=('arial',12,'bold'),width=10,text="Gusssing Number",
                                 bg="yellow",command=gnum).grid(row=4,column=1)
#guessing name button
btngname=Button(f1, padx=16,pady=8,bd=16,fg="black",font=('arial',12,'bold'),width=10,text="Gusssing Name",
                                 bg="slateblue",command=gname).grid(row=4,column=2)
#jumbled word button
btnjw=Button(f1, padx=16,pady=8,bd=16,fg="black",font=('arial',12,'bold'),width=10,text="Jumbled word",
                                 bg="orange",command=jw).grid(row=4,column=3)


#exit button
btnExit=Button(f1, padx=16,pady=8,bd=16,fg="black",font=('arial',12,'bold'),width=10,text="EXIT",
                                 bg="red",command=qExit).grid(row=6,column=2)



 
import random 
intro= int(input("guess a number =  "))
numbers = random.randint(1,9)
actualNum= 3
chances= 5
            
if(intro==actualNum):
    print("Congrats")
if(intro < actualNum):
    chances=chances - 1
    guess1=int(input("enter a larger number :-  "))
    
    if(guess1 < actualNum):
        chances=chances - 1
        guess2=int(input("enter a larger number :-  "))
        
        
        if(guess2 < actualNum):
            chances=chances - 1
            guess3=int(input("enter a larger number :-  "))
            
            if(guess3 < actualNum):
                chances=chances - 1
                guess3=int(input("u lose "))
            if(guess3==actualNum):
                
                print("Congrats")
            if(guess3 > actualNum):
                chances=chances - 1
                guess3=int(input("u lose"))     
                   
               
        if(guess2 > actualNum):
            chances=chances - 1
            guess3=int(input("enter a smaller number :-  "))
           
            if(guess3 < actualNum):
                chances=chances - 1
                print("YOU LOSE!!!!")
            if(guess3==actualNum):
                
                print("Congrats")
            if(guess3 > actualNum):
                chances=chances - 1
                print("YOU LOSE!!!!")
            
           
        if(guess2 == actualNum):
            chances=chances - 1
            guess3=int(input("Congrats"))
    if(guess1 > actualNum):
        chances=chances - 1
        guess2=int(input("enter a smaller number :-  "))
        
        
        if(guess2 < actualNum):
            chances=chances - 1
            guess3=int(input("enter a larger number :-  "))
            
            if(guess3 < actualNum):
                chances=chances - 1
                guess3=int(input("u lose "))
            if(guess3==actualNum):
                
                print("Congrats")
            if(guess3 > actualNum):
                chances=chances - 1
                guess3=int(input("u lose"))     
                   
               
        if(guess2 > actualNum):
            chances=chances - 1
            guess3=int(input("enter a smaller number :-  "))
           
            if(guess3 < actualNum):
                chances=chances - 1
                print("YOU LOSE!!!!")
            if(guess3==actualNum):
                
                print("Congrats")
            if(guess3 > actualNum):
                chances=chances - 1
                print("YOU LOSE!!!!")
            
           
        if(guess2 == actualNum):
            chances=chances - 1
            guess3=int(input("Congrats"))       
    if(guess1 == actualNum):
        print("congrats")       
    # Divide
if(intro > actualNum):
    chances=chances - 1
    guess1=int(input("enter a smaller number :-  "))
    
    if(guess1 < actualNum):
        chances=chances - 1
        guess2=int(input("enter a larger number :-  "))
        
        
        if(guess2 < actualNum):
            chances=chances - 1
            guess3=int(input("enter a larger number :-  "))
            
            if(guess3 < actualNum):
                chances=chances - 1
                guess3=int(input("u lose "))
            if(guess3==actualNum):
                
                print("Congrats")
            if(guess3 > actualNum):
                chances=chances - 1
                guess3=int(input("u lose"))     
                   
               
        if(guess2 > actualNum):
            chances=chances - 1
            guess3=int(input("enter a smaller number :-  "))
           
            if(guess3 < actualNum):
                chances=chances - 1
                print("YOU LOSE!!!!")
            if(guess3==actualNum):
                
                print("Congrats")
            if(guess3 > actualNum):
                chances=chances - 1
                print("YOU LOSE!!!!")
            
           
        if(guess2 == actualNum):
            chances=chances - 1
            guess3=int(input("Congrats"))       
    
    if(guess1 > actualNum):
        chances=chances - 1
        guess2=int(input("enter a smaller number :-  "))
        
        
        if(guess2 < actualNum):
            chances=chances - 1
            guess3=int(input("enter a larger number :-  "))
            
            if(guess3 < actualNum):
                chances=chances - 1
                guess3=int(input("u lose "))
            if(guess3==actualNum):
                
                print("Congrats")
            if(guess3 > actualNum):
                chances=chances - 1
                guess3=int(input("u lose"))     
                   
               
        if(guess2 > actualNum):
            chances=chances - 1
            guess3=int(input("enter a smaller number :-  "))
           
            if(guess3 < actualNum):
                chances=chances - 1
                print("YOU LOSE!!!!")
            if(guess3==actualNum):
                
                print("Congrats")
            if(guess3 > actualNum):
                chances=chances - 1
                print("YOU LOSE!!!!")
            
           
        if(guess2 == actualNum):
            chances=chances - 1
            guess3=int(input("Congrats"))       
    if(guess1 == actualNum):
        print("congrats")     
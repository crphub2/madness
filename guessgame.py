import random
print("guess any number between 0-20")
x=random.randint(0,20)
z='yes'
print(x)
while 'true':
    print("if output is less than guess type'l'or grater type'g' or found type anything")
    le=str(input())
    if le=='l':
         y=random.randint(0,x)
         print(y)
         x=y
    elif le=='g':
         y=random.randint(x,20)
         print(y)
         x=y
    else:
        print("we found your gussing number")
        break
         
         
    
    

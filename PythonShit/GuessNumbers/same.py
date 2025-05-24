import math
import random

num = 50
skip = 50
randnum = 17
tries = 0
print(randnum)

while True:
    print(f"Is {num} your number")
    tries += 1
    if randnum > num:
              
            skip = math.ceil(skip/2)
            num = num + skip  

    elif randnum < num:
            
            skip = math.ceil(skip/2)  
            num = num - skip  

    elif randnum == num:
            break
    
    else:
        print("so silly")

print(f"YEsss, tried {tries} times")


#At the end of this exchange, your program should print out how many guesses it took to get your number.


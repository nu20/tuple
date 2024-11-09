Weather = (1 , 0 , 0 , 0 , 1 , 1 , 0)
sunny = 0
rainy = 0
for i in Weather :
    if(i==1) :
        rainy = rainy + 1
    else :
        sunny = sunny + 1
print("the total of sunny days = " , sunny)
print("the total of rainy days = " , rainy)


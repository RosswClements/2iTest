# In a language of your choice, using all best practice principles you’re aware of, 
# could you please provide code that iterates in multiples of A until X, 
# then in multiples of A + 1 until 2X, then multiples of A + 2 until 3X. 
# Please state any assumptions you’ve made.


#Aussiming that until X means that I should not print anything exceeding X. 

def main():

    a = 2
    iter1 = a 
    iter2 = a+1
    iter3 = a+2
    x = 15
    goal1 = x
    goal2 = x*2
    goal3 = x*3

    print("Multiples of A until X")
    while iter1 <= goal1:
        print(iter1)
        iter1 = a + iter1

    print("Multiples of A+1 until 2X")
    while iter2 <= goal2:
        print(iter2)
        iter2 = (a + 1) + iter2

    print("Multiples of A+2 until 3X")
    while iter3 <= goal3:
        print(iter3)
        iter3 = (a + 2) + iter3
    

main()


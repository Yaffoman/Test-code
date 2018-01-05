def message_repeater(msg):
    num = int(raw_input("How many iterations?"))
    print num*(msg+'\n')

def lessthan(num):
    L = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for element in [i for i in L if i < num]:print element    

print lessthan(num = int(raw_input("Enter number:\t")))
            
        

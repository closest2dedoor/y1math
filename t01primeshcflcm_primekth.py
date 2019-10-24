# What is the kth prime number?

def is_prime(x):
    if x == 2:
        return True
    else:
        for number in range (3,x): 
            if x % number == 0 or x % 2 == 0:
         #print number
                return False
        
        return True

lst = [2]
for i in range(3,k):
    if is_prime(i) == True:
        lst.append(i)
        #print lst
        if len(lst) == 100:
            print lst[9]
            break

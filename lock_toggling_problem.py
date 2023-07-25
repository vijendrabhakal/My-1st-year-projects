'''Que;- At a place there are 100 keys for 100 locks. All the locks are initially in locked state.
If we starts reversing states of locks(if it is locked, then open it and vice versa) in such 
a order that key 1 will reverse states of all the locks present in it's table,likewise all
the keys will do same. What will be the states of all the locks after 100th key operated. '''

'''Ans:- Just take a random number e.g.-56, all it's divisors will perform reverse operation for lock no. 56
factors of 56 are 1*56, 2*28, 14*4, 7*8. so 1 will open the lock and 2 will close it. In this way all the locks will 
remain in closed state at end. Only lock no(perfect square) will ramain open e.g.-16, factors of 16 are 1*16, 2*8, 4*4, 
here first 4 will open the lock but second 4 would not be able to close it as it is repeated and same goes for all perfect
squares. Below there is a code in which array a represents the states of locks with 0 representing closed and 1 representing
open. Initially all the locks are closed, so all the elements in array are zero. then we find perfect square indices and 
assigns them 1.
 '''

def is_a_perfect_square(number):
    if number < 0:
        return False
    sqrt_num = int(number ** 0.5)
    return sqrt_num * sqrt_num == number

a = []
for i in range(101):
    a.append(0)
for i in range(1,101):
    if(is_a_perfect_square(i)):
        a[i] = 1
    print(a[i],i)    
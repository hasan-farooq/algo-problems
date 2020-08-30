


"""
Approach : Dynamic Programming
Complexity : Not known (because I couldn't construct tabulation/memoization yet...)

Example : we'll change the word "calculus" to the word "cluster"

As far I tried, I couldn't find a better solution except Brute-force...

Greedy Approach fails because if we choose the current best choice, in most cases it will not give 
the right cost. The greedy choice will take current best 
But we're not sure if that works fine for whole word...

We've to check all possibilities i.e. at some index we should try insert/delete/replace the word..
Then, we check the best option.


However, this question obeys the principal of optimality. At some index, if we have the 
solution for previous problems, we can just add one more solution (one more instance) and 
we'll get the best till this next instance. So, we can go with Dynammic Programming here...


This recurrence can have error, but this is my attempt...

At some index: (ith index is for calculus & jth is for cluster)

if (ith == jth):
    do nothing
    recurse for (i+1, j+1)
else:
    take the minimum from these:
        //insert
        insert the jth element at ith-1 index
        recurse for (i-1,j)
        //delete
        delete the ith element
        recurse for (i,j+1)         //here i is actually (i+1)th element bcz we deleted the ith one
        //replace
        replace the ith element with jth
        recurse(i+1,j+1)

"""




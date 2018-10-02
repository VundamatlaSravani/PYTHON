#Problem Statement
'''Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird

Input Format
A single line containing a positive integer, .

Output Format
Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0
3

Sample Output 0
Weird'''

n = int(raw_input())
if n%2!=0 or (n%2==0 and n in range(6,21)):
     print("Weird")
else:
    print("Not Weird")


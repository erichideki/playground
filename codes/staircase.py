# https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    for i in range(1, n+1):
         print(("#" * i).rjust(n))

if __name__ == '__main__':
    n = 6
    
    staircase(n)

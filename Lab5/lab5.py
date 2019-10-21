# def eat(n):
#     if n == 1:
#         print('eat',n,end=' ')
#     else:
#         eat(n-1)
#         print('eat',n,end=' ')

# eat(10)

# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n-1)

# print(fac(5))

# def sum1ToN(n):
#     if n == 1:
#         return n
#     else:
#         return n + sum1ToN(n-1)

# print(sum1ToN(4))

# def printNto1(n):
#     if n == 1:
#         print(1)
#     else:
#         print(n,end=' ')
#         printNto1(n-1)

# printNto1(5)

# def print1ToN(n):
#     if n == 1:
#         print(n, end=' ')
#     else:
#         print1ToN(n-1)
#         print(n, end=' ')

# print1ToN('1ToN :',5)

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    
# print('Fibonacci :',fib(5))

# def binarySearch(lo, hi, x, lis):
#     l = lo
#     h = hi
#     mid = int((l+h)/2)
#     if lis[mid] == x:
#         return True
#     elif l == h:
#         return False
#     else:
#         if x > lis[mid]:
#             l = mid + 1
#         elif x < lis[mid]:
#             h = mid - 1
#         return binarySearch(l,h,x,lis)

# l = [2,5,6,8,9,11,13,20,32]
# print(binarySearch(0,8,2,l))

# def move(n, f, t):
#     if n == 1:
#         print('Move from',f,'to',t)
#     else:
#         l = ['A','B','C']
#         f = l.pop(l.index(f))
#         t = l.pop(l.index(t))
#         tmp = l[0]
#         move(n-1,f,tmp)
#         print('Move from',f,'to',t)
#         move(n-1,tmp,t)

# move(5,'A','C')

def sum1(n, l):
    if n == 0:
        return l[0]
    else:
        return l[n-1] + sum1(n-1, l)

print(sum1(3, [1,2,3,4,5,6,7,8]))


# def printSack(sack, maxi):
#     global good
#     global name
#     for i in range(maxi+1):
#         print(name[sack[i]], good[sack[i]], end = ' ')
#     print()

# def pick(sack, i, mLeft, ig):
#     global N
#     global good
#     if ig < N:
#         price = good[ig]
#         if mLeft < price:
#             pick(sack, i, mLeft, ig+1)
#         else:
#             mLeft -= price
#             sack[i] = ig
#             if mLeft == 0:
#                 printSack(sack, i)
#             else:
#                 pick(sack, i+1, mLeft, ig+1)
#             pick(sack, i, mLeft+price, ig+1)

# good = [20,10,5,5,3,2,20,10]
# name = ['soap', 'potato chips', 'loly pop', 'toffy', 'pencil', 'rubber', 'milk', 'cookie']
# N = len(good)

# sack = N*[-1]
# mLeft = 20
# i = 0
# ig = 0
# pick(sack, i, mLeft, ig)


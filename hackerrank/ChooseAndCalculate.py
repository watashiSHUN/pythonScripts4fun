#https://www.hackerrank.com/challenges/choose-and-calculate
def helper(l,k):
    returnDict = {}
    for i in range(len(l)):
        for j in range(i+k-1,len(l)):
            returnDict[j-i-1] = returnDict.get(j-i-1,0) + (l[j]-l[i])
    return returnDict

n,k = [int(x) for x in "100 15".split()]
balls = [int(x) for x in "546 681 5788 2975 7009 371 3545 4861 9821 7086 1626 5665 6557 2652 1723 2891 7391 4741 3834 5065 5182 5477 5865 5190 3937 9109 7378 5186 6305 2799 8414 3204 9832 555 2531 6841 926 6076 8054 747 9514 9680 2764 2423 2332 4488 1667 6076 5581 1853 7493 7115 7330 3358 2305 7619 8820 9684 2805 5125 8835 1220 4681 8667 8127 7212 1860 9053 9640 9914 6153 5507 5947 8917 7930 8279 9757 5949 707 1691 7803 8201 8806 1485 1559 7464 9105 379 3500 1910 1857 2335 9482 2890 7354 3961 103 9214 3015 6095".split()]
balls.sort()
if k == 1:
    print('0')
elif k == n:
    print((balls[-1]-balls[0])%(10**9+7))
else:
    # create a dictionary since it's always something choose k-2
    returnDict = helper(balls,k)
    k_prime = k-2
    last = 1
    returnV = returnDict[k_prime] % (10**9+7)
    for i in range(1,n-2-k_prime+1):
        last = last * (k_prime+i) // i
        returnV = (returnV + (returnDict[k_prime+i]*last)) % (10**9+7)
    print(returnV)

# XXX expected output for testcase 4, 953565723, when I use combinations instead of self producing
# FIXME


# if we know K, constant, not an user input
# balls = [40,30,20,10,1]
# k = 3
#
# for i in range(3):
#     for j in range(i+1,4):
#         for k in range(j+1,5):
#             print(balls[i],balls[j],balls[k],sep="")

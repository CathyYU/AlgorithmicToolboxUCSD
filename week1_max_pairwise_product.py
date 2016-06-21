# Uses python3
# python does not have an integer overflow issues
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

def MaxPairWise(n,a):
    result = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result


# modified algorithm to improve computation efficiency
def MaxPairWiseFast(n,a):
    max1 = -1
    max2 = -1
    result = 0

    for i in range(0, n):
        if (max1 == -1) or (a[i] > a[max1]):
            max1 = i

    for j in range(0, n):
        if (max2 == -1) or (a[j] > a[max2]):
            if j != max1:
                max2 = j
    result = a[max1]*a[max2]
    return result


#result1 = MaxPairWise(n,a)
result2 = MaxPairWiseFast(n,a)

#print(a[-1])
#print(result1)
print(result2)

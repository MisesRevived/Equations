def standardDeviation(a):
    """Calculating standard deviation based on total observations (n) and array with dataset."""
    from math import sqrt
    n = len(a)
    # Finding the average
    avg = 0
    for i in range(0, n):
        avg += float(a[i])
    avg /= n
    # Finding the sum
    sum = 0
    for i in range(0, n):
        sum += float((a[i] - avg) ** 2)
    # Returning standard deviation
    variance = (1.0/(float(n)-1.0))*float(sum)
    stanDev = sqrt(variance)
    print ("The standard deviation of your dataset is " + str(stanDev))

# Creating example array with large but repetitive dataset
arr = []
i = 0
while i < 1263:
    arr.append(0)
    i+=1
while i < 2130:
    arr.append(2)
    i+=1
while i < 2500:
    arr.append(3)
    i+=1
standardDeviation(arr)










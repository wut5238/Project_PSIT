"""FibonacciRecursionV1"""
def main(num):
    """FibonacciRecursionV1"""
    total = 0
    lis = []
    for i in range(1, num+1):
        for j in range(1, i):
            if i % j == 0 or i % j == i:
                total += j
        if total == i:
            lis.append(i)
        total = 0
    print(sum(lis))
main(int(input()))

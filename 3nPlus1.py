"""3nPlus1"""
def main():
    """find amount of all sequence"""
    ans = []
    count = 0
    while 1:
        num = int(input())
        if num == 0:
            break
        while 1:
            if num == 1:
                count += 1
                ans.append(count)
                count = 0
                break
            if num%2 == 0:
                num = num/2
                count += 1
            else:
                num = (num*3)+1
                count += 1
    print(*ans, sep="\n")
main()


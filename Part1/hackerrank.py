def sockMerchant(n, ar):
    # Create a dictionary to count occurrences of each sock
    sock_count = {}
    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1

    # Calculate the number of pairs
    pairs = 0
    for count in sock_count.values():
        pairs += count // 2
    
    return pairs

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

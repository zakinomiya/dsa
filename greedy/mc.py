coins = [10, 5, 1]

def numOfCoins(num: int) -> int:
    c = 0

    for v in coins:
       c += num // v
       num %= v
    
    return c

if __name__ == "__main__":
    print(numOfCoins(int(input())))

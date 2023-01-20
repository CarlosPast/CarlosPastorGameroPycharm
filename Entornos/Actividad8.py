def to_decimal(n):
    num = list(str(n))
    num.reverse()

    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i]) *  2**i
    return decimal

def to_binary(n):
    binary = []

    while n > 0:
        binary.append(str(n%2))
        n//=2
    binary.reverse()
    return "".join(binary)




print(to_decimal(10110))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal("10110")))


def is_htts(n):
    if len(str(n)) % 2 == 0:
        return "NO"
    for digit in str(n):
        if int(digit) % 2 == 0:
            return "NO"
    return "YES"


n = int(input())
result = is_htts(n)
print(result)

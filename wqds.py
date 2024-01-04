def is_HTTS(n):
    # N sonining uzunligi toq bo'lishi kerak
    if len(str(n)) % 2 == 0:
        return "NO"

    # N sonining barcha raqamlari toq bo'lishi kerak
    for digit in str(n):
        if int(digit) % 2 == 0:
            return "NO"

    # Agar yuqorida qaytarilmasa, N soni HTTS shartlarini qanoatlantirmoqda
    return "YES"


# N sonini olish
n = int(input())

# Natijani chiqarish
result = is_HTTS(n)
print(result)

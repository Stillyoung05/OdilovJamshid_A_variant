from random import randint
from faker import Faker


with open("test1.txt", "w") as tst1:
    fk = Faker()
    amount = int(input("Enter data amount: "))
    for i in range(1, amount + 1):
        tst1.write(f"{i}. {fk.name()} {randint(11, 99)}\n")

rdbl = open("test1.txt", "r")
for _ in range(amount):
    ln = rdbl.readline()
    age = ln.split()[3]
    l_name = ln.split()[2]
    vowels = ["a", "e", "i", "o", "u", "y"]


    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if len(l_name) >= 8 and int(age) % 2 == 0 and is_prime(int(age)) and l_name[-1] not in vowels:
        with open("test2.txt", "w") as tst2:
            for _ in range(amount):
                tst2.write(f"{ln}\n")




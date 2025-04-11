q = int(input("Kitni queries karni hain? "))
while q > 0:
    number = int(input("Kaunsa number check karna hai? "))
    print(f"{number} occurs {hash[number]} times")
    q -= 1
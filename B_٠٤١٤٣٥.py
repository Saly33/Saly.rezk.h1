def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)
number = eval(input("أدخل عدداً لحساب العاملي الخاص به: "))
f = calculate_factorial(number)
print(f"العاملي للعدد {number} هو {f}")

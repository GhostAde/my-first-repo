user_age = int(input("Enter your age: "))
subscription_age = int(input("Enter the age of subscription: "))
if user_age>=25:
    print("You are eligible for the subscription.")
elif subscription_age >= 2:
        print("You are eligible for a discount.")
else:
    print("You are not eligible for the discount.")

# Ticket price calculation based on age group

age = int(input("Enter age : "))
if (age < 0 & age == 0):
    print("Enter a valid age")
elif (age > 18):
    print(f"Ticket price per head is 100")
else:
    print(f"Ticket price per head is 80")
# Electricity Bill Calculator
RATE = 12.90

#Validate cutomer name

while True:
    name = input("Enter customer name: ")
    
    if name.strip() != "":
        break
    else:
        print("Invalid name, name cannot be empty.")
        
#Validate previous value

while True:
    previous = float(input("Enter previous meter reading: "))
    
    if previous >= 0:
        break
    else:
        print("The previous meter reading cannot be less than 0.")
        
#Validate current value

while True: 
    current = float(input("Enter current meter reading: "))
    
    if current >= previous:
        break
    else:
        print("Current meter reading should not be less than the previous one.")


consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading# Electricity Bill Calculator
RATE = 12.90

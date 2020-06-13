# 2. WAP that takes out time and take another input as your regular outtime.
# If out time is greater than regular outtime then show the overtime,
# sample input:
# enter your regular outtime: 6
# enter your outtime: 8
# sample output:
# Overtime 2 hour

print("Our Regular Office Working Hours: 8 Hrs.")
regular_time = 8
overtime = int(input("Enter Your Total Working Time in Hours: "))
ot_calc = overtime-regular_time
print("Your Overtime is", +ot_calc)

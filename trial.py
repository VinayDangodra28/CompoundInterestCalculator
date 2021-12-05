from calculator import *

p = int(input("Enter Princilpe Value:-\n"))
r = float(input("Enter rate of interest per annum:-\n"))
# n = int(input("Enter number of times compound in a tenure:-\n"))
t = int(input("Enter number of years:-\n"))
abc = input("Enter 'y' for yearly deposits and 'm' for monthly deposits")
if abc == "m":
    m = float(input("Enter monthly contributions:-\n"))
elif abc == "y":
    m = float(input("Enter yearly contributions:-\n"))
    m = m/12
xyz = input("Enter 'y' for yearly, 'h' for half yearly, 'q' for quarterly, 'm' for monthly, 'd' for daily compoundation")
if xyz == "y":
    n = 1
elif xyz =="h":
    n = 2
elif xyz =="q":
    n = 4
elif xyz =="m":
    n = 12
elif xyz =="d":
    n = 365

output = ci(p, n, r, t, m)
print(output)
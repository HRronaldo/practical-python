# sears.py
# 一天早晨，您出去在芝加哥的西尔斯大厦（Sears tower）旁的人行道上放一张美钞。 
# 此后的每一天，您出门都要付两倍的账单数。 一叠钞票超过塔的高度需要多长时间？ 
bill_thickness = 0.11 * 0.001 # Meters(0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)

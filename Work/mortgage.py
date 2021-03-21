# mortgage.py
#
# Exercise 1.7

# Dave已决定进行一笔为期30年的固定利率抵押贷款500,000美元与Guido的按揭，
# 股票投资和比特币交易公司。利率为5％，每月还款额为2684.11美元。 
# 计算Dave将拥有的总金额 在抵押期内支付：

# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0

# while principal > 0:
#     principal = principal * (1 + rate / 12) - payment
#     total_paid = total_paid + payment

# print('Total paid', total_paid)


# 假设Dave在抵押贷款的前12个月每月额外支付$ 1000？ 

# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# month = 0

# while principal > 0:
#     month += 1

#     if month <= 12:
#         payment1 = payment + 1000
#         principal = principal * (1 + rate / 12) - payment1
#         total_paid = total_paid + payment1
#     else:
#         principal = principal * (1 + rate / 12) - payment
#         total_paid = total_paid + payment

#     print(month, round(total_paid,2), round(principal, 2))

# print('Months', month)
# print('Total paid', round(total_paid, 2))


# 如果Dave从抵押贷款的第5年开始，为期4年每月支付额外的$ 1000，他将支付多少？ 

# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# month = 0

# extra_payment = 1000
# extra_payment_start_month = 49
# extra_payment_end_month = 97

# while principal > 0:
#     month += 1
#     principal = principal * (1 + rate / 12) - payment
#     total_paid = total_paid + payment

#     if month >= extra_payment_start_month and month <= extra_payment_end_month:
#         principal = principal - extra_payment
#         total_paid = total_paid + extra_payment

#     print(month, round(total_paid,2), round(principal, 2))
    
# print('Total paid', round(total_paid, 2))
# print('Months', month)


# 修改程序以打印出一个表格，其中显示了月份，到目前为止已支付的总额以及剩余的本金。

# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# month = 0

# extra_payment = 1000
# extra_payment_start_month = 61
# extra_payment_end_month = 108

# while principal > 0:
#     month += 1
#     principal = principal * (1 + rate / 12) - payment
#     total_paid = total_paid + payment

#     if month >= extra_payment_start_month and month <= extra_payment_end_month:
#         principal = principal - extra_payment
#         total_paid = total_paid + extra_payment

#     print(month, round(total_paid,2), round(principal, 2))

# print('Total paid', round(total_paid, 2))
# print('Months', month)


# 修复最后的多付款项数额

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    month += 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
 
    if principal < 0:
        principal = 0

    print(month, round(total_paid,2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)

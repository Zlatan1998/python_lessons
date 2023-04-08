net_cash_flow = float(input("Enter the value of net cash flow:  "))
discount_rate = float(input("Enter the value of discount rate:  "))
time = float(input("Enter the value of time:  "))
net_present_value = (net_cash_flow / (1 + discount_rate)) * time
print(net_present_value)
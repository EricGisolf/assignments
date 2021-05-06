# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
leek_price_str = str(leek_price)

print('Leek is '+leek_price_str+' euro per kilo.')

four_leeks = 'leek 4'
four_int = int(four_leeks[four_leeks.find('4')])

sum_total = four_int * leek_price
print(sum_total)

broccoli_price = 2.34 # euro/kg
broccoli_order = 'broccoli 1.6'

total_broccoli_price = broccoli_price * float(broccoli_order[broccoli_order.find('1.6'):(broccoli_order.find('1.6')+3)])
total_broccoli_price = str(round(total_broccoli_price,2))

print('1.6kg broccoli costs '+total_broccoli_price+'e')
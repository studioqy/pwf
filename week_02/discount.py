from datetime import datetime


current_time = datetime.now()

day = current_time.isoweekday()

#subtotal = float(input("Please enter the subtotal:\n>"))
subtotal = 0
cont = True
num = 1
while cont:
  message = "Enter the price of item " + str(num) + "\nenter \"done\" to check out.\n>"
  response = input(message)
  if response != "done":
    price = float(response)
    response = int(input("How many of this item do you have?\n>"))
    subtotal += response * price
    num += 1
  else:
    cont = False





if subtotal >= 50 and (day == 2 or day == 3):
  new_total = subtotal * .90
  discount = subtotal * .1
  print(f"Original total: ${subtotal:.2f}\nDiscount: -${discount:.2f}")
elif (day == 2 or day == 3):
  difference = 50 - subtotal
  print(f"Today is a discount day!\nSpend ${difference:.2f} more to receive a 10% discount!")
  new_total = subtotal
else:
  new_total = subtotal

tax = new_total * 0.06
final = new_total + tax


print(f"Subtotal: ${new_total:.2f}\nTax: ${tax:.2f}\nTotal: ${final:.2f}")
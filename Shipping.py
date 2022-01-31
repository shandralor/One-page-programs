weight= int(input("What is the weight of your package in lbs? "))


print(weight)


def ground_shipping(weight):
  price = 0
  if weight <= 2:
      price = weight * 1.5 +20
      return price
  elif weight <= 6:
      price = weight * 3 + 20
      return price
  elif weight <=10:
      price = weight * 4 + 20
      return price
  else:
      price = weight * 4.75 + 20
      return price
ground_shipping_premium = 125

def drone_shipping(weight):
  price = 0
  if weight <= 2:
      price = weight * 4.5
      return price
  elif weight <= 6:
      price = weight * 9
      return price
  elif weight <=10:
      price = weight * 12
      return price
  else:
      price = weight * 14.25
      return price


print(ground_shipping(weight))
print(ground_shipping_premium)
print(drone_shipping(weight))


list_prices = [ground_shipping(weight),ground_shipping_premium,drone_shipping(weight)]
list_prices.sort()

print(list_prices)

if list_prices[0] == ground_shipping(weight):
  print(f"Ground shipping normal is best for you with a cost of : {ground_shipping(weight)}")
elif list_prices[0] == drone_shipping(weight):
  print(f"Drone shipping is best for you with a cost of : {drone_shipping(weight)}")
else:
  print(f"Ground shipping premium is best for you with a cost of : {ground_shipping_premium}")

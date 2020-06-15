supermarket = int(input())

for i in range(supermarket):
  value, grams = input().split()
  grams = int(grams)
  value = float(value)
  kg = float(grams/1000)

  endValue = value*(1000/grams)
  
  
  if (i == 0):
    price = endValue
  else:
    if ( endValue < price):
      price = endValue

print("%.2f"%price)


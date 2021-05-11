weight = 41.5

# Ground Shipping
if weight <= 2:
  ground = (weight * 1.50) + 20.00
elif weight <= 6:
  ground = (weight * 3.00) + 20.00
elif weight <= 10:
  ground = (weight * 4.00) + 20.00
else:
  ground = (weight * 4.75) + 20.00
print("Ground Shipping is $", ground)

# Premium Shipping
premium = 125.00
print("Premium Shipping is $", premium)

# Drone Shipping
if weight <= 2:
  drone = weight * 4.50
elif weight <= 6:
  drone = weight * 9.00
elif weight <= 10:
  drone = weight * 12.00
else:
  drone = weight * 14.25
  print("Drone Shipping is $", drone)

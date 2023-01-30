weight = 41.5
cost = 0

#Ground Shipping
if weight <= 2:
    ground_shipping_cost = 20 + weight * 1.50
elif weight <= 6:
    ground_shipping_cost = 20 + weight * 3.00
elif weight <= 10:
    ground_shipping_cost = 20 + weight * 4.00
else:
    ground_shipping_cost = 20 + weight * 4.75

#Ground Shipping Premium
ground_shipping_premium_cost = 125.00

#Drone Shipping
if weight <= 2:
    drone_shipping_cost = weight * 4.50
elif weight <= 6:
    drone_shipping_cost = weight * 9.00
elif weight <= 10:
    drone_shipping_cost = weight * 12.00
else:
    drone_shipping_cost = weight * 14.25


print(ground_shipping_cost)
print(ground_shipping_premium_cost)
print(drone_shipping_cost)

if ground_shipping_cost <= ground_shipping_premium_cost and ground_shipping_cost <= drone_shipping_cost:
    cost = ground_shipping_cost
elif ground_shipping_premium_cost <= ground_shipping_cost and ground_shipping_premium_cost <= drone_shipping_cost:
    cost = ground_shipping_premium_cost
elif drone_shipping_cost <= ground_shipping_premium_cost and drone_shipping_cost <= ground_shipping_cost:
    cost = drone_shipping_cost

print(cost)
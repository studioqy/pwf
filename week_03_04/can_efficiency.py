from math import pi

def main():
  names = []
  radii = []
  heights = []
  prices = []
  best_efficiency = 0
  best_cost = 0
  
  with open("cans.csv") as cans_data:
    for line in cans_data:
      data = line.split(",")
      names.append(data[0])
      radii.append(float(data[1]))
      heights.append(float(data[2]))
      prices.append(float(data[3]))

  for i in range(len(names)):
    efficiency = can_efficiency(radii[i],heights[i])
    cost_efficiency = can_cost_efficiency(radii[i], heights[i], prices[i])
    if efficiency > best_efficiency:
      best_efficiency = efficiency
      best_ef_name = names[i]
    if cost_efficiency > best_cost:
      best_cost = cost_efficiency
      best_cost_name = names[i]
    print(f"{names[i]:<12} {efficiency:.1f} {cost_efficiency:.0f}")
    
  print(f"Best Storage: {best_ef_name} {best_efficiency:.1f}\nBest Cost: {best_cost_name} {best_cost:.0f}")
  

def can_surface_area(radius, height):
  return 2 * pi * radius * (radius + height)

def can_volume(radius, height):
  return pi * radius ** 2 * height

def can_efficiency(radius, height):
  return can_volume(radius, height)/can_surface_area(radius, height)

def can_cost_efficiency(radius, height, cost):
  return can_volume(radius, height)/cost
  
main()
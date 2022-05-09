keys = ['apple', 'berry', 'cherry']
values = [5, 1, 3]
# print(keys[1], ':', values[1])

fruits_inventory = {"apple": 5,"berry": 1,"cherry": 3} 
fruits_inventory["durian"] = 1
fruits_inventory["Apple"] = fruits_inventory["apple"] + 3
# print(fruits_inventory)
del fruits_inventory["Apple"]
print(fruits_inventory)
total_num_fruit_in_fridge = 0
for fruit_values in fruits_inventory.values():
  total_num_fruit_in_fridge += fruit_values

print(f"{total_num_fruit_in_fridge}")


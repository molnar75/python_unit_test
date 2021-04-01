x = [5, 10, 3, 22, 14, 30, 50, 8]

def get_minimum(list):
  min = list[0]
  
  for i in range(1, len(list)):
    if(min > list[i]):
        min = list[i]
  
  return min

print(get_minimum(x))


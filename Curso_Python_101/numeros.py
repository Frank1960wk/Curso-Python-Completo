numero = [1,2,3,4,5,6,7]

def square(num):
    resultado= num**2
    return resultado

def check_even(num):
  return num%2 == 0

for item in map(square, numero):
  print(item)
print(list(map(square,numero)))

for n in filter (check_even,numero):
  print(n)

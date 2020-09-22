# def calorie_calculator(name, get_calorie, spend_calorie):
  #  if get_calorie > spend_calorie:
   #     msg = name + ' getting fat'
   # else:
   #     msg = name + ' lose weight'
  #  return msg

# person = ['Masha', 1900, 1200]
#
# print(calorie_calculator(*person))
# print(calorie_calculator('Sasha', 2000, 2150))

def some(*args):
    result = 0
    for a in args:
        result += a
    print(result)

some(3, 12, 12, 3143, 123, 123, 4)
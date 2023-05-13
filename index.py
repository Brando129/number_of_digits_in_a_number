"""Create a function that will return an integer number corresponding
to the amount of digits in the given integer num"""

def count_digits(num):

  if not isinstance(num, int):
    raise TypeError("num must be an integer")

  return len(str(num))

print(count_digits(12345))
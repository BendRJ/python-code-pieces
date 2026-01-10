# Generators are functions that can pause and resume their execution. 
# When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

#idempotence is calling a function with the same function results in the function
#f(f(x)) --- > f(x)  # here calling the function f(f(x)) is similar to calling f(x)
#Below is the example
print(abs(abs(abs(-10))))
# abs(-10) == 10
# abs(10) == 10
# abs(10) == 10


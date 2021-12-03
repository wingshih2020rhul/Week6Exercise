num1 = float(input("num1: "))
num2 = float(input("num2: "))
try:
    print(num1 / num2)
except ZeroDivisionError:
    print("undefined")


try:
    print("hi")
    print(1/0)
except ZeroDivisionError:
    print("dllm")
finally:
    print("dllm again")
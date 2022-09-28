# All Import Statements
import sympy as sy
import time

# Head Section
print("***Welcome to Reduction Calculator By Raj***\n")

print("This is a CLI based calculator that will help you to solve the n-th order integration of Sin-Cos-Tan functions.\nThis calculator is based on the Reduction Rule of Integration.\n")

time.sleep(2)

print("This all functions are working under limit 0 to pi/2\nExcept Tan^n(x)\n\nSelect Your Work-Space\n\nEnter 1 for use Sin^n(x) or Cos^n(x)\nEnter 2 for use Sin^n(x)*Cos^n(x)\nEnter 3 for use Tan^n(x)\nEnter 0 for Exit!\n")

# Main Body
mode = int(input("Enter Your Work-Space No.: "))
# Sin(x) or Cos(x)
if mode == 1:
  print("You Select Sin^n(x) or Cos^n(x) Calculator\n")
  n = int(input("Enter the Power of Sin(x) or Cos(x): "))
  lower_limit = 0
  upper_limit = sy.pi/2
  def f(x, n):
    return sy.cos(x)**n
  x = sy.Symbol('x')
  result = sy.integrate(f(x, n), (x, lower_limit,upper_limit))
  print(f"Ans: Sin^{n}(x) = {result} Also, Cos^{n}(x) = {result}\n")
  print("Thanks for using Reduction Calculator.")

# Sin(x)Cos(x)
elif mode == 2:
  print("You Select Sin^n(x)*Cos^n(x)\n")
  m = int(input("Enter the Power of Sin(x): "))
  n = int(input("Enter the Power of Cos(x): "))
  lower_limit = 0
  upper_limit = sy.pi/2
  def f(x, m):
    return sy.sin(x)**m
  def g(x, n):
    return sy.cos(x)**n
  x = sy.Symbol('x')
  result = sy.integrate(f(x,m)*g(x,n),(x,   lower_limit,upper_limit))
  print(f"Ans: Sin^{m}(x)*Cos^{n}(x) = {result}\n")
  print("Thanks for using Reduction Calculator.")

# Tan(x)
elif mode == 3:
  print("You Select Tan^n(x)\n")
  print("Default limit 0 to pi/4\n")
  n = int(input("Enter the Power of Tan(x): "))
  lower_limit = 0
  upper_limit =sy.pi/4
  def f(x, n):
    return sy.tan(x)**n
  x = sy.Symbol('x')
  result = sy.integrate(f(x, n), (x, lower_limit, upper_limit))
  print(f"Ans: Tan^{n}(x) = {result}\n")
  print("Thanks for using Reduction Calculator.")

elif mode == 0:
  print("Thanks for using Reduction Calculator.\nExit!")
else:
  print(f"Input Error!\nPlease Check Your Input Value...Work-Space: {mode} does not exist.")
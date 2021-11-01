original = float(input("Starting Number: "))
final = float(input("Final Number: "))
print("\n")

calc = final / original
if calc == 1:
  print("No Profit")
if calc > 1:
  ans_calc = calc * 100
  ans2 = ans_calc - 100
  print(ans2, "% Increase")
if calc < 1:
  ans_calc2 = calc - 1
  ans3 = ans_calc2 * -100
  print(ans3, "% Decrease")

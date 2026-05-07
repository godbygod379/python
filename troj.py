A = float(input("Enter value for A: "))
B = float(input("Enter value for B: "))
C = float(input("Enter value for C: "))

if A + B <= C or A + C <= B or B + C <= A:
   print("not possible to create a triangle")
elif A + B > C and A + C > B and B + C > A:
   print("possible to create a triangle")
if A == B == C:
   print("rovnostranny triangle")
elif A == B or B == C or A == C:
   print("rovnoramenny triangle")
else:  print("roznostranny triangle")



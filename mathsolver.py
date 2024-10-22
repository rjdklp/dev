import time
import random

print("Which Function Do You Need?")
time.sleep(0.4)
print("Press 1 for Line Equation Solver")
time.sleep(0.4)
print("Press 2 for Diamond Problem Solver")
time.sleep(0.4)
print("Press 3 for Linear Equation Solver")
time.sleep(0.4)
what_function = int(input("Choose an option by typing the designated number, "))
time.sleep(0.4)
print(what_function)
if what_function == 1:
   more_equations = int(input("How Many Equations Do You Have? "))
   for i in range(more_equations):
       x1 = float(input("What is x1? "))
       y1 = float(input("What is y1? "))
       x2 = float(input("What is x2? "))
       y2 = float(input("What is y2? "))
      
       final_y_1 = y2 - y1
       final_x_1 = x2 - x1
       slope = final_y_1/final_x_1
       str_slope = str(slope)
       print("The Slope is, " + str_slope)
      
       for_b_x = float(input("What is the X Value? "))
       for_b_y = float(input("What is the Y Value? "))
       negative_slope = slope * -1
       negative_mx = negative_slope * for_b_x
       intercept_y_final = for_b_y + negative_mx
       str_intercept_y_final = str(intercept_y_final)
       print("The Y Intercept Is, " + str_intercept_y_final)
  
       print("__________________________________________________________________________")
       print("The Equation Is...")
       print("Y = " + str_slope + "x + " + str_intercept_y_final)
      
       print("Checking Slope Validity...")
       print("__________________________________________________________________________")
       for_check_slope_y = for_b_y - intercept_y_final
        
       if for_check_slope_y / for_b_x == slope:
        print("The Slope Is Correct! ")


       else:
        print("The Slope Is Not Correct, Try Different Values ")


       print("__________________________________________________________________________")
      
if what_function == 2:
       more_diamonds = int(input("How Many Diamond Problems Do You Have? "))
       for i in range(more_diamonds):
        X_diamond = float(input("What is the X Value? "))
        Y_diamond = float(input("What is the Y Value? "))
      
        diamond_top = X_diamond * Y_diamond
        diamond_bottom = X_diamond + Y_diamond
        str_diamond_top = str(diamond_top)
        str_diamond_bottom = str(diamond_bottom)
      
        print("The top for the problem is, " + str_diamond_top)
        print("The bottom for the problem is, " + str_diamond_bottom)

if what_function == 3:
        left_side_x = float(input("How many Xs are on the left side? "))
        left_side_number = float(input("What is the number on the left side? "))

        right_side_x = float(input("How many Xs are on the right side? "))
        right_side_number = float(input("What is the number on the right side? "))

        left_total = left_side_x * left_side_number
        right_total = right_side_x * right_side_number

        print("__________________________________________________________________________")
        print("Solving Equation...")
        time.sleep(1)
        print("__________________________________________________________________________")

        sub_x = left_side_x - right_side_x
        sub_cons = left_side_number - right_side_number

        if sub_x == 0:
            if sub_cons == 0:
                print("Infinite Solutions")
            else:
                print("No Solution")
        else:
            x_value = sub_cons / sub_x
            str_x_value = str(x_value)
            print(str_x_value + " Is the value for X.") 

print("__________________________________________________________________________")
input("Press Enter To Exit")
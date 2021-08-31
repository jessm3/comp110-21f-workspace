""" My Numeric Operators Program """

__author__ = "730250025"

left_hand_side: str = input("Left-hand side: ")
right_hand_side: str = input("Right-hand side: ")
first_number: int = int(left_hand_side)
second_number: int = int(right_hand_side)
power_number: int = (first_number ** second_number)
str_power_number: str = str(power_number)
print(left_hand_side + " ** " + right_hand_side + " is " + str_power_number)
divide_number: float = (first_number / second_number)
str_divide_number: str = str(divide_number)
print(left_hand_side + " / " + right_hand_side + " is " + str_divide_number)
integer_divide_number: int = (first_number // second_number)
str_integer_divide_number: str = str(integer_divide_number)
print(left_hand_side + " // " + right_hand_side + " is " + str_integer_divide_number)
remainder_number: int = (first_number % second_number)
str_remainder_number: str = str(remainder_number)
print(left_hand_side + " % " + right_hand_side + " is " + str_remainder_number)
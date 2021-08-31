""" My Relational Operators Program """

__author__ = "730250025"

left_hand_side: str = input("Left-hand side ")
right_hand_side: str = input("Right-hand side ")
first_number: int = int(left_hand_side)
second_number: int = int(right_hand_side)
less_than_number: int = int(first_number < second_number)
bool_less_than_number: bool = bool(less_than_number)
str_less_than_number: str = str(bool_less_than_number)
print(left_hand_side + " < " + right_hand_side + " is " + str_less_than_number)
at_least_number: int = int(first_number >= second_number)
bool_at_least_number: bool = bool(at_least_number)
str_at_least_number: str = str(bool_at_least_number)
print(left_hand_side + " >= " + right_hand_side + " is " + str_at_least_number)
equal_to_number: int = int(first_number == second_number)
bool_equal_to_number: bool = bool(equal_to_number)
str_equal_to_number: str = str(bool_equal_to_number)
print(left_hand_side + " == " + right_hand_side + " is " + str_equal_to_number)
not_equal_to_number: int = int(first_number != second_number)
bool_not_equal_to_number: bool = bool(not_equal_to_number)
str_not_equal_to_number: str = str(bool_not_equal_to_number)
print(left_hand_side + " != " + right_hand_side + " is " + str_not_equal_to_number)
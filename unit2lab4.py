"""
Program: Gas and Oil Purchase Calculator
Description: This program calculates the total cost of gas or oil purchases, applies volume discounts, calculates provincial GST, and displays a summary table.
Date: 2026-15-30
Group Name: Group 4

"""
from typing import Final
OIL_PRICE: Final = 1.25
OIL_LITRES_PER_CASE: Final = 12
GAS_PRICE: Final = 1.05
DISCOUNT_THRESHOLD_OIL: Final = 6
DISCOUNT_THRESHOLD_GAS: Final = 2000
AB_OR_BC_GST: Final = 0.05
ON_GST: Final = 0.13
OTHERS_GST: Final = 0.15

banner_text = "*** Welcome to Gas Station Program! ***"
border_length = len(banner_text)

print("-" * border_length)
print(banner_text)
print("-" * border_length)

print("Please select the type of purchase:")
print("G: Gas\nO: Oil")
user_choice = input(">>> ")

if user_choice.upper() != "G" and user_choice.upper() != "O":
    print("Invalid input, you should enter g/G or o/O")

elif user_choice.upper() == "O":
    num_of_cases = int(input("Enter # of cases of Oil : "))
    if num_of_cases < 0:
        print("Number of oil cases should be > 0")
        exit()
    else:
        product_name = "Oil"
        quantity = num_of_cases * OIL_LITRES_PER_CASE
        price_before_discount = quantity * OIL_PRICE
        
        if num_of_cases > DISCOUNT_THRESHOLD_OIL:
            price_after_discount = quantity * (OIL_PRICE * 0.9)
        else:
            price_after_discount = price_before_discount
            
        total_cost_before_tax = price_after_discount
        
        province = input("Please enter the 2 letters province abbreviation: ")
        if province.upper() == "AB" or province.upper() == "BC":
            gst = total_cost_before_tax * AB_OR_BC_GST
        elif province.upper() == "ON":
            gst = total_cost_before_tax * ON_GST
        else:
            gst = total_cost_before_tax * OTHERS_GST
            
        total_cost = total_cost_before_tax + gst

        # Table Output
        separator = "-" * 105
        print(separator)
        print(f"{'Product':<10} {'# Of Litres':<15} {'Price Before Discount':<24} {'Price After Discount':<22} {'GST':<8} {'Total Price'}")
        print(f"{product_name:<10} {quantity:<15} {price_before_discount:<24.1f} {price_after_discount:<22.1f} {gst:<8.2f} {total_cost:.2f}")
        print(separator)
        
        print("Thanks for your business, Good Bye")    

elif user_choice.upper() == "G":
    num_of_litres = int(input("Enter the number of litres of gas : "))
    if num_of_litres < 0:
        print("Number of gas litres should be > 0")
        exit()
    else:
        product_name = "Gas"
        quantity = num_of_litres
        price_before_discount = quantity * GAS_PRICE
        
        if num_of_litres > DISCOUNT_THRESHOLD_GAS:
            price_after_discount = quantity * (GAS_PRICE * 0.9)
        else:
            price_after_discount = price_before_discount
            
        total_cost_before_tax = price_after_discount
        
        province = input("Please enter the 2 letters province abbreviation: ")
        if province.upper() == "AB" or province.upper() == "BC":
            gst = total_cost_before_tax * AB_OR_BC_GST
        elif province.upper() == "ON":
            gst = total_cost_before_tax * ON_GST
        else:
            gst = total_cost_before_tax * OTHERS_GST
            
        total_cost = total_cost_before_tax + gst  

        # Table Output
        separator = "-" * 105
        print(separator)
        print(f"{'Product':<10} {'# Of Litres':<15} {'Price Before Discount':<24} {'Price After Discount':<22} {'GST':<8} {'Total Price'}")
        print(f"{product_name:<10} {quantity:<15} {price_before_discount:<24.1f} {price_after_discount:<22.1f} {gst:<8.2f} {total_cost:.2f}")
        print(separator)

    print("Thanks for your business, Good Bye")
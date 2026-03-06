###################################################################################
# Computer Project 01
#
#   Description
#   This program is designed to process integers from
#   a user-specified file and generate an output by converting
#   rods to meters, feet, miles, furlongs, and minutes.
#
#     The script performs the following tasks:
#
#    1. Prompt the user to enter a floating-point value representing a distance in rods.
#    2. Reprint that value using the strings provided below.
#    3. Convert the value to the following measurement units below.
###################################################################################


#Variable is created to instruct user to input a rod number
num_str1 = float(input("\n:~Input rods ~:"))


#output is generated using users previous input
print ("\nYour value is", num_str1, "rods.")

#conversions form rods to meters, ft, miles, furlongs, and minutes
#the float number num_str1 is used to be converted for each unit
meters = num_str1 * 5.0292

feet = num_str1 * 5.0292 / 0.3048

miles = num_str1* 5.0292 / 1609.34

furlongs = num_str1 / 40

rods_flt = num_str1

minutes_flt = num_str1 * 5.0292 / 1609.34 /3.1 *60


print ("\nConversions:")
print ("Meters:" , round(meters,3))
print ("Feet:" , round(feet,3))
print ("Miles:" , round(miles,3))
print ("Furlongs:" , round(furlongs,3))
print ("Time to walk", round (rods_flt, 3) , "rods is", round (minutes_flt,3) , "minutes." )



# use the following strings in your input statements
"\n:~Input rods ~:"

# the following 2 strings should be in the same print statement
#seperated by the input rods
"\nYour value is"
"rods."

# use the following strings in your print statements
"\nConversions:"
"Meters:"
"Feet:"
"Miles:"
"Furlongs:"
"Time to walk", rods_flt, "rods is", minutes_flt, "minutes."
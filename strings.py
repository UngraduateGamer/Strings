name="Rahul"
""" triple single or double quotes used for multiple line strings and comments """
story=""" Twinkle Twinkle Little Star
How are Wonder what you are
"""
print(story)

# # index
# string is the sequence of characters 
# r a h u l
# 0 1 2 3 4
# -5 -4 -3 -2 -1

print(name[-5])
print(name[1])
print(name[2])
print(name[3])
print(name[-1])

print(name[-4:-2]) 
# or lower is the same output
print(name[len(name)-4:len(name)-2])

# slicing
print(name[0:5]) # 0 inclluding 4 excluding

# len function len(str)
str='rahul'
print(len(str))

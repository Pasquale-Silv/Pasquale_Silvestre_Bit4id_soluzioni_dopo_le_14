from Q1 import shift_left, shift_right, shift

print(shift_left("1011"))
print(shift_left("0111"))
string1 = shift_left("1011")
for i in range(2):
    print(string1)
    string1 = shift_left(string1)

string2 = shift_right(string1)
print("right:")
print(string2)
for i in range(2):
    print(shift_right(string2))
    string2 = shift_right(string2)

print("------------------")

print("1011")
print(shift("1011", 'left', 2))
print("Inverso:", shift("1110", 'right', 2))
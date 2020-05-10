from functions import square

name=input();
print(f"Welcome, {name}!")



version = (1.0, 2.0, 3.0)
admin =["Gedeon", "Andrew", "Musk"]
for admins in list(admin):
	print(f"Our Admins are {admins}")
	pass
networth={"Gedeon":24, "Andrew":34, "Musk":78}
print(networth)
for x in range(0,9):
	if x%2==0:
		print(f"even Numbers are {x}")
		print(f" and square is {square(x)}")

s=set()
s.add(3)
s.add(7)
print(f"The defined set is: {s}")
if name == "Gedeon":
	print("Your authorised")
elif name == "gedeon":
	print("your authorised")
else:
	print("Your not authroised")

def square(x):
	return x*x

def main():
	for x in range(0,9):
		if x%2==0:
			print(f"even Numbers are {x}")
			print(f"THe square of {x} the number is {square(x)}")

if __name__=="__main__":
	main()
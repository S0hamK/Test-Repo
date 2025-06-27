print("This is a test code file")
print("HELLO WORLD")

"""Module to calculate the area of a circle and print Hello World."""

def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    pi = 3.14
    return pi * radius * radius

def main():
    """Main function to execute the script."""
    print("Hello World")
    radius = 5
    print(area_of_circle(radius))

if __name__ == "__main__":
    main()

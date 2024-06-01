def perimeter(length,breadth):
    print(f"Perimeter = {2*(length+breadth)}")

def area(length,breadth):
    print(f"Area = {length * breadth}")

def volume(length,breadth,height):
    print(f"Volume = {length*breadth*height}")

def two_D(n):
    if n==1:
        l= int(input("Enter the length: "))
        area(l,l)
        perimeter(l,l)
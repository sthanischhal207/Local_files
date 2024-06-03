import math

pi = math.pi

def perimeter(length,breadth):
    return 2*(length+breadth)

def area(length,breadth):
    return length * breadth

def volume(length,breadth,height):
    return length*breadth*height

def cperimeter(radius):
    return 2*pi*radius

def carea(radius):
    return  pi*pow(radius,2)

def cvolume(radius):
    return (4/3)*pi*pow(radius,3)

def two_D(n):
    if n==1:
        choose = int(input("CHOOSE:\n1)Square\n2)Rectangle\n3)trapezium\n4)Circle\n5)Triangle\n"))
        match choose:
            case 1:
                l = float(input("Enter length: "))
                print(f"Perimeter = {perimeter(l,l)}")
                print(f"Area = {area(l,l)}")
            case 2:
                l = float(input("Enter length: "))
                b = float(input("Enter breadth: "))
                print(f"Perimeter = {perimeter(l,b)}")
                print(f"Area = {area(l,b)}")
            case 3:
                h = float(input("Enter height: "))
                l = float(input("Enter First Length: ")) + float(input("Enter Second Length: "))
                print(f"Area = {0.5*area(h,l)}")
            case 4:
                r = float(input("Enter radius: "))
                print(f"Perimeter = {cperimeter(r)}")
                print(f"Area = {carea(r)}")

def three_D(n):
    if n==2:
        choose = int(input("CHOOSE:\n1)Cube\n2)Cuboid\n3)Cylinder\n4)Sphere\n5)Semi-Sphere\n6)Pyramid\n7)Cone\n8)Triangular Prism\n"))
        match choose:
            case 1:
                l = float(input("Enter length: "))
                print(f"Perimeter = {3*perimeter(l,l)}")
                print(f"Area = {6*area(l,l)}")
                print(f"Volume = {volume(l,l,l)}")
            case 2:
                l = float(input("Enter length: "))
                b = float(input("Enter breadth: "))
                h = float(input("Enter height: "))
                print(f"Perimeter = {2*perimeter(l,b) + 4*h}")
                print(f"Area = {2*(area(l,b) + area(l,h) + area(b,h))}")
                print(f"Volume = {volume(l,b,h)}")
            case 3:
                r = float(input("Enter radius: "))
                h = float(input("Enter height: "))
                print(f"Total Surface Area = {2*carea(r) + cperimeter(r)*h}")
                print(f"Curved Surface Area = {cperimeter(r)*h}")
                print(f"Volume = {carea(r)*h}")

def main():
    print("-------Welcome to Geometric Calculator-------")
    choose = int(input("CHOOSE:\n1)Two Dimensional\n2)Three Dimensional\n"))
    two_D(choose)
    three_D(choose)

main()
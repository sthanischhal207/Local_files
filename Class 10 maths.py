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

def triangle():
    choose = int(input(("CHOOSE:\n1)Equilateral\n2)Isosceles\n3)Scalene\n")))
    if choose == 1 :
        a = float(input("Enter side length:"))
        print(f"Perimeter: {3*a}")
        print(f"Area: {(math.sqrt(3)/4)*pow(a,2)}")
    elif choose == 2:
        a = float(input("Enter equal side length:"))
        b = float(input("Enter unequal side length:"))
        print(f"Perimeter: {2*a+b}")
        print(f"Area: {(b/2)*math.sqrt(pow(a,2)-pow(b/2,2))}")
    elif choose == 3:
        a = float(input("Enter side 1 length:"))
        b = float(input("Enter side 2 length:"))
        c = float(input("Enter side 3 length:"))
        print(f"Perimeter: {a+b+c}")
        s = (a+b+c)/2
        print(f"Area: {math.sqrt(s*(s-a)*(s-b)*(s-c))}")


def two_D():
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
            case 5:
                triangle()
            case _:
                two_D()

def three_D():
        choose = int(input("CHOOSE:\n1)Cube\n2)Cuboid\n3)Cylinder\n4)Sphere\n5)Semi-Sphere\n"))
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
            case 4:
                r = float(input("Enter radius:"))
                print(f"Total Surface Area: {4*carea(r)}")
                print(f"Volume: {cvolume(r)}")
            case 5:
                r = float(input("Enter radius:"))
                print(f"Curved Surface Area: {2*carea(r)}")
                print(f"Total Surface Area: {3*carea(r)}")
                print(f"Volume: {cvolume(r)/2}")
                
            case _:
                three_D()

def main():
    while True:
        print("-------Welcome to Geometric Calculator-------")
        choose = int(input("CHOOSE:\n1)Two Dimensional\n2)Three Dimensional\n"))
        if choose == 1:
            two_D()
        elif choose == 2: 
            three_D()
        else:
            main()

        if 'y' in input("WANNA USE MORE?(y/n)\n").lower():
            main()
        break

if __name__ == "__main__":
    main()

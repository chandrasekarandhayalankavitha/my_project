
import math
d = math.pi
def areaofcircle(r):
    ans1 = d*r*r
    return ans1
def areaofrectangle(l, b):
    ans2 = l * b
    return ans2

if __name__ == "__main__":
    print("This is executed from prog6basemain module")
    ans1 = areaofcircle(10)
    print("Area of Circle:", ans1)
    ans2 = areaofrectangle(10, 20)
    print("Area of Rectangle:", ans2)

else:
    print("This is executed from prog6childmain module")
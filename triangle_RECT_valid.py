class shapes:
    
    def init(self):
        pass

    def triangle(self,triangle_sides):
        self.triangle_sides = triangle_sides
        side1,side2,side3 = self.triangle_sides[0],self.triangle_sides[1],self.triangle_sides[2]
        if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
            return "\nValid Triangle"
        else:
            return "\nInvalid Triangle"

    def rectangle(self,rectangle_sides):
        self.rectangle_sides = rectangle_sides
        side1,side2,side3,side4 = self.rectangle_sides[0],self.rectangle_sides[1],self.rectangle_sides[2],self.rectangle_sides[3]
        if side1==side3 and side2==side4 :
            return "\nValid Rectangle"
        else:
            return "\nInvalid Rectangle"


shape = shapes()
triangle_values = input("").split(" ")
print("\n")
rectangle_values = input("").split(" ")
tri_val=[]
rect_val=[]

if len(triangle_values)==3:
    try:
        for values in triangle_values:
            temp = int(values)
            tri_val.append(temp)
        print(shape.triangle(tri_val))
    except :
        print("Invalid Inputs for triangle checking")
else:
    print("Invalid input for tiangle checking")

if len(rectangle_values)==4:
    try:
        for values in rectangle_values:
            temp = int(values)
            rect_val.append(temp)
        print(shape.rectangle(rect_val))
    except :
        print("Invalid Inputs for rectangle checking")
else:
    print("Invalid inputs for rectangle checking") 
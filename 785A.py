inputs=[]
sides=0
n = int(input())
for i in range(n):
    inputs.append(input())
for item in inputs:
    if(item=="Tetrahedron"):
        sides = sides + 4
    elif(item=="Cube"):
        sides = sides + 6
    elif(item=="Octahedron"):
        sides = sides + 8
    elif(item=="Dodecahedron"):
        sides = sides + 12
    elif(item=="Icosahedron"):
        sides = sides + 20
    else:
        print("wrong input")
print(sides)
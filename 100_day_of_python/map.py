row1 = ["X","X","X"]
row2 = ["X","X","X"]
row3 = ["X","X","X"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
coordinates = input("enter coordinates: ")
hor_col = int(coordinates[0])-1 #3 = 2
ver_row = int(coordinates[1])-1 #2 = 1
map[ver_row][hor_col] = "$$"
print(f"{row1}\n{row2}\n{row3}")
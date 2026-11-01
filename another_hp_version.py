hpr = float(input("Enter the horsepower:"))
wt = float(input("Enter the weight of the vehicle:"))
pr = float(input("Enter the price of the vehicle:"))
etr = hpr/wt*1000
shp = hpr/pr
score = 0
if etr > 180: score+= 1
if shp >10: score+= 2
match score:
    case 0:
        print("The vehicle has low performance and low value.")
    case 1:
        print("The vehicle hasperformance but low value.")
    case 2:
        print("The vehicle has low performance but high value.")
    case 3:
        print("The vehicle has high performance and high value.")

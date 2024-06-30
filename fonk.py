import math
points=[(1,2),(3,4),(5,6)]
def euclideanDistance(point,point1):
    return math.sqrt((point[0]-point1[0]**2 +(point[1]-point1[1])))

distances=[]

for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance =euclideanDistance(points[i],points[j])
        distances.append((distance))

minimum =min(distance)
print(minimum)
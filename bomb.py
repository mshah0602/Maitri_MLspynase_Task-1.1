import numpy as np
region=np.array([[1,0,0,0,1], 
[1,0,1,1,1], 
[1,1,0,1,1], 
[1,0,1,1,0], 
[0,1,0,1,1] ])
#m=3
#half=m//2
#targerted_region=region[1:4,1:4]
def bombarded_region(region,m,):
    n=region.shape[0]
    center=m//2
    max_region=0
    best_region=None
    best_targerted_region=None
    damage_coordinates=[]


    for r in range(center,n-center):
        for c in range(center,n-center):
            targerted_region=region[r-center:r+center+1, c-center:c+center+1]


        if region[r,c]==1:
            damage=np.sum(targerted_region)
            if damage>max_region:
                max_region=damage
                best_region=(r,c)
                best_targerted_region=targerted_region
                damage_coordinates=[]
                for i in range(targerted_region.shape[0]):
                    for j in range(targerted_region.shape[1]):
                        if targerted_region[i,j]==1:
                            damage_coordinates.append((r-center+i,c-center+j))
    return max_region,damage_coordinates,best_targerted_region,best_region
max_region,damage_coordinates,best_targerted_region,best_region=bombarded_region(region,3)

print("damaged co-ordinates: " , damage_coordinates)
print("max_region: ", max_region)
print("best targerted region: " , best_targerted_region)
print("best region : " , best_region)
    


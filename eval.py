from math import hypot 

derive_weight = 1
it_weight = 1/200
dist_weight = 1/20

def eval(path, target, it, obstacle):
    derive = 0
    dist_min = 10000
    for i in range(len(path)-1):
        derive += (hypot(path[i][0] - target[0],path[i][1] - target[1])-hypot(path[i+1][0] - target[0],path[i+1][1] - target[1]))/it
        for ob in obstacle:
            dist_min = min(dist_min, hypot(path[i][0] - ob[0],path[i][1] - ob[1]))

    return  dist_weight*(400-dist_min) + it_weight*it + hypot(path[-1][0]-target[0],path[-1][0]-target[0])*dist_weight + derive_weight*derive

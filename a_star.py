from queue import PriorityQueue
import copy

que = PriorityQueue()
fisrt = [[1,2,6], [0,4,3], [0,7,5]]
last = [[1,2,3], [0,0,4], [7,6,5]]

def f(start, goal, level):
    return h(start,goal) + level

def h(start,goal):
    temp = 0
    for i in range(0,3):
        for j in range(0,3):
            if start[i][j] != goal[i][j]:
                temp += 1
    return temp

def change(arr, x1, y1, x2, y2, level):
    if(0 <= x2 and x2 < 3 and 0 <= y2 and y2 < 3 and arr[x2][y2] != 0):
        temp = arr[x1][y1]
        arr[x1][y1] = arr[x2][y2]
        arr[x2][y2] = temp
        level = level + 1
        newval = [f(arr, last, level),arr,level]
        que.put(newval)

def process():
    val = [f(fisrt, last, 0),fisrt,0]
    que.put(val)
    while True:
        [p,q,r] = que.get()
        print("fval : ", p)
        print("Index : ", q)
        print("Level : ", r)
        print("")
        if(q == last):
            break   
        for i in range(0, 3):
            for j in range(0, 3): 
                if q[i][j] == 0:
                    var = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
                    for k in var:
                        tq = copy.deepcopy(q)
                        change(tq, i, j, k[0], k[1], r)         

process()
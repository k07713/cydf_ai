import copy

first = [[1,2,6], ['*',4,3], ['*',7,5]]
last = [[1,2,3], ['*','*',4], [7,6,5]]
limit = 0
check = 0
finish = 0

def change(arr, x1, y1, x2, y2):
    global check
    check = 0
    if(0 <= x2 and x2 < 3 and 0 <= y2 and y2 < 3 and arr[x2][y2] != '*'):
        temp = arr[x1][y1]
        arr[x1][y1] = arr[x2][y2]
        arr[x2][y2] = temp
        check = 1

def dfs(arr, level):
    global limit, finish
    if level > limit:
        return
    if arr == last:
        finish = 1
    if finish == 1:
        return
    for i in range(0, 3):
        for j in range(0, 3): 
            if arr[i][j] == '*':
                var = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
                for k in var:
                    p = copy.deepcopy(arr)
                    change(p, i, j, k[0], k[1])
                    if check == 1:
                        q = copy.deepcopy(p)
                        dfs(q, level+1)

def process():
    global limit
    while(1):
        cur = copy.deepcopy(first)
        print(limit)
        dfs(cur, 0)
        if(finish):
            print("Gotit")
            break
        limit = limit + 1

process()

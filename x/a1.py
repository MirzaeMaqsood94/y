
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['G'],
    'D':[],
    'E':['F'],
    'F':[],
    'G':[]
}
def iddfs(source,destination,graph,depth):
    for i in graph:
        if dfs(source,destination,graph,depth):
            return True
        else:
            return False

def dfs(source,destination,graph,depth):
    print("current node",source)
    if source == destination:
        return True
    if depth <= 0:
        return False
    for child in graph[source]:              
        if dfs(child,destination,graph,depth-1):    
            return True
    return False

if iddfs('E','G',graph,4):
    print("path exists")
else:
    print("path doesn't exists")


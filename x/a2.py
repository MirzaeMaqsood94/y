def best_first_search(start, target):
    closed = list()

    queue = [start]
    visited = set()
    while queue:
        node = queue[0]
        closed.append(queue.pop(0))
        
       # print(node, end=" ") # optional
        print("closed nodes")
        print(closed)
        visited.add(node)
        if node == target:
            print("PATH: ")
            for element in closed:
            	print(element,end="->")
            print("\nGoal node is found.")
            return
        else:
            for child in tree[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)

            print(" \nunsorted queue")
            print(queue)        
            queue.sort(key=lambda x: cost_tree[x])
            print("sorted queue")
            print(queue)
            
            print("=================================\n")
    print("\nGoal node is not found.")
    

tree = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": [], "E": [], "F": [], "G": []}
cost_tree = {"A": 0, "B": 4, "C": 2, "D": 6, "E": 10, "F": 11, "G": 3}
best_first_search(start="A", target="G")

def bfs(graph, root, forb):
    #keep a list of visited nodes
    visited = [root]
    #queue to save the adjacencies
    queue = [(0,)+root]
    #while queue has elements to visit the adjacencies
    while queue:
        d,Ox,Oy = queue[0]
        flagFob = False
        # verify adjacencies for vertice v
        for (x,y) in graph[(Ox,Oy)]:
            #if node has never been visited
            if (d+1,x,y) in forb:
                flagFob = True

            if (x,y) not in visited and (d+1,x,y) not in forb:
                #mark as visited
                visited.append((x,y))
                #add in queue to explore your adjacencies
                queue.append((d+1,x,y))
        if flagFob:
            queue.append((d+1,Ox,Oy))
        #remove first element from queue, because it's already been visited
        queue.pop(0)
    #returns the elements in the order they were visited
    return d

def nextLine():
    line = ''
    while line == '':
        line = input().strip()
    return line

def main():
    while True:
        n_line = nextLine()

        nv,nh = [int(x) for x in n_line.split(' ')]
        graph = {}
        forbidden = set()
        for i in range(nv):
            for j in range(nh):
                graph[(i,j)] = set()
                if i > 0:
                    graph[(i,j)].add((i-1,j))
                if j > 0:
                    graph[(i,j)].add((i,j-1))
                if i < nv-1:
                    graph[(i,j)].add((i+1,j))
                if j < nh-1:
                    graph[(i,j)].add((i,j+1))
        delet = nextLine()

        n_del = int(delet)
        for i in range(n_del):
            coord = nextLine()

            x1,y1,x2,y2 = [int(x) for x in coord.split(' ')]
            graph[(x1,y1)] -= {(x2,y2)} #set {}

        query = nextLine()

        n_quer = int(query)
        for _ in range(n_quer):
            fb = nextLine()
            t,x,y = map(int,fb.split(' '))
            tup = (t,x,y)
            forbidden.add(tup)
        print(bfs(graph,(0,0),forbidden))

try:
    main()
except EOFError:
    pass

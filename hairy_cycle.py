def DFS(AdjMat, vertex, visited):
  visited[vertex] = True
  for i in range(verts):
    if AdjMat[vertex][i] == 1 and visited[i] is False:
      DFS(AdjMat, i, visited)
  
def isConnected(AdjMat, verts) -> bool:
  visited = [False]*verts
  start = 0
  DFS(AdjMat, start, visited)
  ## starting vertex is 0, randomly
  if False in visited:  ## could also keep count for efficiency
    return False
  return True

verts = eval(input("enter number of vertices: "))
edges = eval(input("enter number of edges: "))

# make Adjacency matrix of the graph
AdjMat = [[0]*verts for i in range(verts)]

## i will keep track of degrees because i will need them
degs = [0]*verts
## let's assume first it is a hairy cycle
hairy_flag = True

for i in range(edges):
    a, b = (input("Enter edge: ")).split(" ")
    a = eval(a)
    b = eval(b)
    AdjMat[a-1][b-1] = 1
    AdjMat[b-1][a-1] = 1
    degs[a-1] += 1
    degs[b-1] += 1
    ## to save time, check one of my conditions as i go.
    ## all degrees are either 1, 2, or 3
    if degs[a-1] < 1 or degs[a-1] > 3 or  degs[b-1] < 1 or degs[b-1] > 3:
      hairy_flag = False
      print("Failed condition 1")
      break

## if it passed, move on to other conditions

## there should be the same number of vertices as edges.
## i could have checked this after getting verts and edges to save time
## but i thought i should finish getting the input first

if hairy_flag and verts == edges:
  ## any vertex of degree 2 must not be adjacent to a vertex of degree 1
  ## to eliminate graphs like these: one of the vertices of the cycle is connected to a chain of vertices
  for i, elt in enumerate(degs):
    if not hairy_flag:
      print("Failed condition 3")
      break
    elif elt == 1:
      for j in range(verts):
        if AdjMat[i][j] == 1 and degs[j] == 2:
          hairy_flag = False
          break
    elif elt == 2:  ## could've gone without this elif
      for j in range(verts):
        if AdjMat[i][j] == 1 and degs[j] == 1:
          hairy_flag = False
          break

  ## the final check is connectivity,
  ## as a graph could just be a bunch of disjoint cycles
  if hairy_flag and isConnected(AdjMat, verts) is False:
    hairy_flag = False
    print("Failed condition 4")
elif hairy_flag:
  hairy_flag = False
  print("Failed condition 2")  ## verts != egdes

if hairy_flag:
  print("Yes, the input graph has the structure I was assigned")
else:
  print("No, the input graph doesn’t have the structure I was assigned")

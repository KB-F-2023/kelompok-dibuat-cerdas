#inisialisasi state awal
start_state = [[1,2,0],
               [4,5,3],
               [7,8,6]]

#inisialisasi state goal
goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]

#mencari indeks posisi elemen dalam matrix
def find_index(matrix, element):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return i, j

#mencari nilai heuristik dengan menghitung jumlah elemen yang tidak berada pada posisi goal
def heuristic(state):
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                h += 1
    return h

#mencari solusi menggunakan algoritma DFS
def dfs(state, depth, max_depth, path):
    if state == goal_state:
        return True, path
    if depth == max_depth:
        return False, []
    x, y = find_index(state, 0)
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for move in moves:
        i, j = move
        if i >= 0 and i < len(state) and j >= 0 and j < len(state[i]):
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[i][j] = new_state[i][j], new_state[x][y]
            if heuristic(new_state) <= max_depth - depth:
                result, new_path = dfs(new_state, depth+1, max_depth, path + [new_state])
                if result:
                    return True, new_path
    return False, []

#menampilkan solusi
depth = 0
found = False
path = [start_state]
while not found:
    found, path = dfs(start_state, 0, depth, path)
    depth += 1
print("Depth: ", depth-1)
print("Steps: ")
for step in path:
    for row in step:
        print(row)
    print()

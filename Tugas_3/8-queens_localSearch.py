import random


def calculate_conflicts(board):
    """
    Fungsi untuk menghitung jumlah konflik pada board yang diberikan
    """
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j]:
                conflicts += 1
            offset = j - i
            if board[i] == board[j] - offset or board[i] == board[j] + offset:
                conflicts += 1
    return conflicts

def get_random_board(n):
    """
    Fungsi untuk menghasilkan sebuah board acak dengan n queen
    """
    board = list(range(n))
    random.shuffle(board)
    return board

def get_neighbour_boards(board):
    """
    Fungsi untuk menghasilkan semua kemungkinan tetangga dari board yang diberikan
    """
    neighbour_boards = []
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            neighbour = board.copy()
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbour_boards.append(neighbour)
    return neighbour_boards

def local_search(n, max_iterations):
    """
    Fungsi utama untuk menyelesaikan 8 Queen dengan local search
    """
    current_board = get_random_board(n)
    current_conflicts = calculate_conflicts(current_board)
    for i in range(max_iterations):
        if current_conflicts == 0:
            # Jika tidak ada konflik, maka solusi sudah ditemukan
            return current_board
        neighbour_boards = get_neighbour_boards(current_board)
        best_neighbour = None
        best_neighbour_conflicts = n*n
        for neighbour in neighbour_boards:
            neighbour_conflicts = calculate_conflicts(neighbour)
            if neighbour_conflicts < best_neighbour_conflicts:
                best_neighbour = neighbour
                best_neighbour_conflicts = neighbour_conflicts
        if best_neighbour_conflicts >= current_conflicts:
            # Jika tidak ada tetangga yang lebih baik, maka berhenti
            return current_board
        current_board = best_neighbour
        current_conflicts = best_neighbour_conflicts
    # Jika sudah mencapai maksimum iterasi, kembalikan board terbaik yang ditemukan
    return current_board

# Fungsi untuk mencetak board dalam bentuk matriks
def print_board(board):
    n = len(board)
    for i in range(n):
        row = ["."]*n
        row[board[i]] = "Q"
        print(" ".join(row))

# Contoh penggunaan
solution = local_search(8, 1000)
if solution:
    print_board(solution)
else:
    print("Solusi tidak ditemukan dalam 1000 iterasi")

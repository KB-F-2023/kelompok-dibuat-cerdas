import random

# Ukuran papan catur
board_size = 8

# Jumlah populasi
population_size = 50

# Jumlah generasi
max_generations = 1500

# Probabilitas mutasi
mutation_rate = 0.6

def initial_population(size):
    """
    Fungsi untuk menghasilkan populasi awal
    """
    population = []
    for i in range(size):
        chromosome = [random.randint(0, board_size-1) for j in range(board_size)]
        population.append(chromosome)
    return population

def fitness(chromosome):
    """
    Fungsi untuk menghitung nilai fitness
    """
    attacks = 0
    for i in range(board_size):
        for j in range(i+1, board_size):
            if chromosome[i] == chromosome[j]:
                attacks += 1
            elif abs(i-j) == abs(chromosome[i]-chromosome[j]):
                attacks += 1
    return board_size*(board_size-1)/2 - attacks

def selection(population):
    """
    Fungsi untuk memilih kandidat solusi terbaik
    """
    fitnesses = [fitness(chromosome) for chromosome in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness/total_fitness for fitness in fitnesses]
    selected_index = random.choices(range(len(population)), weights=probabilities)[0]
    return population[selected_index]

def crossover(parent1, parent2):
    """
    Fungsi untuk melakukan operasi crossover
    """
    crossover_point = random.randint(0, board_size-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(chromosome):
    """
    Fungsi untuk melakukan mutasi
    """
    mutated_chromosome = chromosome[:]
    if random.random() < mutation_rate:
        index1, index2 = random.sample(range(board_size), 2)
        mutated_chromosome[index1], mutated_chromosome[index2] = \
            mutated_chromosome[index2], mutated_chromosome[index1]
    return mutated_chromosome

def genetic_algorithm():
    """
    Fungsi untuk menjalankan algoritma genetik
    """
    # Inisialisasi populasi awal
    population = initial_population(population_size)

    # Iterasi sebanyak max_generations
    for generation in range(max_generations):
        # Seleksi orang tua
        parent1 = selection(population)
        parent2 = selection(population)
        while parent2 == parent1:
            parent2 = selection(population)

        # Operasi crossover
        child1, child2 = crossover(parent1, parent2)

        # Mutasi
        child1 = mutation(child1)
        child2 = mutation(child2)

        # Evaluasi fitness
        children_fitness = [fitness(child1), fitness(child2)]

        # Seleksi kelangsungan hidup
        worst_index = population.index(min(population, key=fitness))
        if children_fitness[0] > children_fitness[1]:
            if children_fitness[0] > fitness(population[worst_index]):
                population[worst_index] = child1
        else:
            if children_fitness[1] > fitness(population[worst_index]):
                population[worst_index] = child2

        # Cek apakah sudah ditemukan solusi
        best_index = population.index(max(population, key=fitness))
        if fitness(population[best_index]) == board_size*(board_size-1)/2:
            return population[best_index], generation

    # Jika tidak ditemukan solusi
    best_index = population.index(max(population, key=fitness))
    return population[best_index], max_generations

# Jalankan algoritma genetik
solution, generations = genetic_algorithm()

# Cetak hasil
if fitness(solution) == board_size*(board_size-1)/2:
    print("Solusi ditemukan pada generasi ke-", generations)
    for i in range(board_size):
        print("."*solution[i] + "Q" + "."*(board_size-solution[i]-1))
else:
    print("Solusi tidak ditemukan.")


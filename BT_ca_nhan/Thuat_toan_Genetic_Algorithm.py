# Thuat_toan_Genetic.py
import random
import numpy as np

N = 8   # số quân hậu = kích thước bàn cờ
POP_SIZE = 100
MUTATION_RATE = 0.2
MAX_GENERATIONS = 1000
SHOW_INTERVAL = 5   # lưu trạng thái mỗi 5 thế hệ

# -----------------------------
def fitness(chromosome):
    non_attacking = 0
    total_pairs = (N * (N - 1)) // 2
    for i in range(N):
        for j in range(i+1, N):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking / total_pairs

def state_to_numpy(state):
    # Chuyển cấu hình list thành mảng numpy 8x8
    arr = np.zeros((N, N), dtype=int)
    for col, row in enumerate(state):
        arr[row, col] = 1
    return arr

# -----------------------------
def init_population():
    return [ [random.randint(0, N-1) for _ in range(N)] for _ in range(POP_SIZE) ]

def selection(population, fitnesses):
    total_fit = sum(fitnesses)
    pick = random.uniform(0, total_fit)
    current = 0
    for chrom, fit in zip(population, fitnesses):
        current += fit
        if current >= pick:
            return chrom
    return population[-1]

def crossover(parent1, parent2):
    point = random.randint(1, N-2)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        col = random.randint(0, N-1)
        row = random.randint(0, N-1)
        chromosome[col] = row
    return chromosome

# -----------------------------
def genetic_algorithm():
    steps = []   # lưu các trạng thái để hiển thị
    population = init_population()

    for generation in range(MAX_GENERATIONS):
        fitnesses = [fitness(chrom) for chrom in population]

        best_idx = fitnesses.index(max(fitnesses))
        best_state = population[best_idx]

        # chỉ lưu trạng thái mỗi SHOW_INTERVAL thế hệ
        if generation % SHOW_INTERVAL == 0:
            steps.append(state_to_numpy(best_state))

        if max(fitnesses) == 1.0:   # tìm thấy nghiệm hoàn hảo
            steps.append(state_to_numpy(best_state))  # lưu nghiệm cuối
            return steps, best_state

        new_population = []
        for _ in range(POP_SIZE):
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    return steps, None

# -----------------------------
def get_steps():
    steps, _ = genetic_algorithm()
    return steps

def get_solution_arr():
    steps, solution = genetic_algorithm()
    if solution:
        return state_to_numpy(solution)
    return None

#rint(get_solution_arr())
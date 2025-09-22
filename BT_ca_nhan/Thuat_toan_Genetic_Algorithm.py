# Nguon: Tham khao tu AI
# Nguyen Van Hoai - 20110107

import random
import numpy as np
import time

N = 8   # số quân hậu = kích thước bàn cờ
POP_SIZE = 100
MUTATION_RATE = 0.2
MAX_GENERATIONS = 1000
SHOW_INTERVAL = 5   # lưu trạng thái mỗi 5 thế hệ

# -----------------------------
def fitness(chromosome):
    # Tỉ lệ các cặp quân hậu không tấn công nhau
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

def genetic_algorithm():
    # Thuật toán Di Truyền (Genetic Algorithm) cho 8 quân hậu.
    # Trả về (steps, solution, step_count, total_time)

    start_time = time.time()
    steps = []
    step_count = 0

    population = init_population()

    for generation in range(MAX_GENERATIONS):
        fitnesses = [fitness(chrom) for chrom in population]

        best_idx = fitnesses.index(max(fitnesses))
        best_state = population[best_idx]

        # lưu trạng thái mỗi SHOW_INTERVAL thế hệ
        if generation % SHOW_INTERVAL == 0:
            steps.append(state_to_numpy(best_state))
            step_count += 1

        if max(fitnesses) == 1.0:   # tìm thấy nghiệm hoàn hảo
            steps.append(state_to_numpy(best_state))  # lưu nghiệm cuối
            step_count += 1
            total_time = time.time() - start_time
            return steps, best_state, step_count, total_time

        new_population = []
        for _ in range(POP_SIZE):
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    total_time = time.time() - start_time
    return steps, None, step_count, total_time

def get_solution_arr():
    # Trả về solution dạng numpy array hoặc None
    _, solution, _, _ = genetic_algorithm()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    # Trả về toàn bộ steps, step_count và total_time
    steps, _, step_count, total_time = genetic_algorithm()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)

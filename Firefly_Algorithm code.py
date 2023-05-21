import random
import math

# Define the objective function
def objective_function(x, y):
    return x**2 + y**2  # Example objective function: minimize x^2 + y^2

# Define the parameters
num_fireflies = 50
num_iterations = 100
lower_bound = -10
upper_bound = 10
alpha = 0.2  # Attraction coefficient
beta0 = 1.0  # Initial attractiveness
gamma = 0.1  # Light absorption coefficient

# Generate random initial solutions
solutions = []
for _ in range(num_fireflies):
    x = random.uniform(lower_bound, upper_bound)
    y = random.uniform(lower_bound, upper_bound)
    intensity = objective_function(x, y)
    solutions.append((x, y, intensity))

# Define the Firefly Algorithm
def firefly_algorithm():
    for iteration in range(num_iterations):
        for i in range(num_fireflies):
            for j in range(num_fireflies):
                if solutions[j][2] < solutions[i][2]:
                    distance = calculate_distance(solutions[i][0], solutions[i][1], solutions[j][0], solutions[j][1])
                    attractiveness = calculate_attraction(beta0, distance)

                    x_diff = attractiveness * (solutions[j][0] - solutions[i][0])
                    y_diff = attractiveness * (solutions[j][1] - solutions[i][1])

                    solutions[i] = (
                        solutions[i][0] + alpha * x_diff,
                        solutions[i][1] + alpha * y_diff,
                        objective_function(solutions[i][0] + alpha * x_diff, solutions[i][1] + alpha * y_diff)
                    )

        # Find the best solution in each iteration
        best_solution = min(solutions, key=lambda x: x[2])
        print("Iteration:", iteration + 1)
        print("Best solution: (x = {}, y = {})".format(best_solution[0], best_solution[1]))
        print("Best fitness:", best_solution[2])
        print()

    # Find the best solution
    best_solution = min(solutions, key=lambda x: x[2])
    return best_solution

# Calculate the Euclidean distance between two solutions
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Calculate the attraction based on attractiveness and distance
def calculate_attraction(beta, distance):
    attraction = beta * math.exp(-gamma * distance**2)
    return attraction

# Run the Firefly Algorithm
best_solution = firefly_algorithm()

# Print the best solution and its fitness
print("Final Best solution: (x = {}, y = {})".format(best_solution[0], best_solution[1]))
print("Final Best fitness:", best_solution[2])

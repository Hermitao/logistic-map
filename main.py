import matplotlib.pyplot as plt

iterations = 750*5
change = 0.001
rate = 1.0
current_x = 0.5
equilibrium_gen = 28

def logistic_map(r, x):
    return r * x * (1 - x)

values = []

for i in range(iterations):
    if i % 2 == 0:
        equilibrium_gen -= 1
    else:
        equilibrium_gen += 1
    pop = current_x
    for j in range(equilibrium_gen):
        pop = logistic_map(rate, pop)
    rate += change
    if pop <= 0 or pop == float("inf") or pop == float("-inf"):
        values.append(0)
    values.append(pop)

print(values)

plt.plot(values, marker='o', linestyle='none')
plt.title('Logistic Map')
plt.xlabel('iteration')
plt.ylabel('population')

plt.show()
    


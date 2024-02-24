import matplotlib.pyplot as plt

# print(plt.style.available)

input_values= [i*0.1 for i in range(1, 100)]
squares = [i**2 for i in input_values]

plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(labelsize=14)
plt.show()

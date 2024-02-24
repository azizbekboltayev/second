import matplotlib.pyplot as plt

x_values = range(-50, 50)
y_values = [i**3 for i in x_values]
# plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, s = 1)

ax.set_title("Cube numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cubbe of Value", fontsize = 14)
ax.tick_params(labelsize = 14)

ax.axis([0, 500, 0, 125_000])
# ax.ticklabel_format(style = 'plain')

plt.show()
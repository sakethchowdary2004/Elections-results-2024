import matplotlib.pyplot as plt
import numpy as np

# Data
alliances = ['NDA', 'INDIA', 'OTH']
seats_2019 = [360, 119, 64]
seats_2024 = [293, 234, 16]
changes = [-67, +115, -48]

# Plotting the bar chart
x = np.arange(len(alliances))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, seats_2019, width, label='2019')
rects2 = ax.bar(x + width/2, seats_2024, width, label='2024')

# Adding text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Alliance')
ax.set_ylabel('Seats Won')
ax.set_title('Seat Changes in Lok Sabha Elections (2019 vs 2024)')
ax.set_xticks(x)
ax.set_xticklabels(alliances)
ax.legend()

# Adding data labels
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

# Annotating the changes
for i, change in enumerate(changes):
    ax.annotate(f'{change:+}',
                xy=(x[i], max(seats_2019[i], seats_2024[i]) + 5),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom', color='red', fontweight='bold')

fig.tight_layout()

plt.show()

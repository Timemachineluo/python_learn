from die import Die
import matplotlib.pyplot as plt

die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
print(results)
frequencies = [] 
for value in range(1, die.num_sides+1): 
    frequency = results.count(value) 
    frequencies.append(frequency) 
print(frequencies)

plt.bar(range(1,len(frequencies)+1),frequencies)
# plt.title = "Results of rolling one D6 1000 times."
# plt.x_title = "Result"
# plt.y_title = "Frequency of Result"
plt.show()
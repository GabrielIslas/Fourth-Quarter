import matplotlib.pyplot as plt

def sequence1():
    s = [1, 2]
    for i in range(2, 30):
        s.append((s[i-1] + s[i-2]) * 0.5)
    return s

print(sequence1())
plt.plot(sequence1())
plt.show()
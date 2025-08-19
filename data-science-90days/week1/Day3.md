
### 📅 **Day 3: Mini Project — Weather Stats**

#### 🎯 Goals

* Use what you’ve learned to simulate and analyze data

---

#### 💡 Project Idea

> Simulate 7 days of temperature readings and calculate:

* Average temperature
* Highest and lowest
* How different the temps were (standard deviation)

---

#### ✍️ Step-by-Step

```python
import numpy as np

# Simulate temperatures
temps = np.array([30, 31, 32, 29, 35, 33, 34])

# Calculations
average = np.mean(temps)
minimum = np.min(temps)
maximum = np.max(temps)
std_dev = np.std(temps)

print("Average temp:", average)
print("Max temp:", maximum)
print("Min temp:", minimum)
print("Temp spread:", std_dev)
```

---

#### ✅ Practice Ideas

* Try entering temps from `input()` instead of hardcoding
* Use a loop to collect 7 values from the user

---

#### 📚 Resources

* [NumPy Crash Course – freeCodeCamp](https://www.youtube.com/watch?v=QUT1VHiLmmI)
* [NumPy Docs - Beginner Guide](https://numpy.org/doc/stable/user/absolute_beginners.html)

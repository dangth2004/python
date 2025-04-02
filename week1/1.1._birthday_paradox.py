n = int(input())

if n < 2:
    probability = 0.0
elif n >= 365:
    probability = 1.0
else:
    prob_no_match = 1.0
    for i in range(n):
        prob_no_match *= (365 - i) / 365
    probability = (1 - prob_no_match) * 100

print(f"{probability:.10f} %")

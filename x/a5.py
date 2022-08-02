weights = [0, 0, 0]
inputs = ((-1, -1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, 1))
expected = (-1, -1, -1, 1)

print("X1\tX2\t\tW1\t\tW2\t\tBias")
for i in range(4):
    x1, x2, bias = inputs[i]
    weights[0] += x1 * expected[i]
    weights[1] += x2 * expected[i]
    weights[2] += bias * expected[i]
    print(f"{x1:2}{x2:4}{round(weights[0],2):8}\t{round(weights[1],2):7}\t{round(weights[2],2):7}")

print("\nOutput of AND Gate for W1, W2 and Bias :")
print("X1\t\tX2\t\tOutput")
for i in range(4):
    print(f"{inputs[i][0]:2}\t\t{inputs[i][1]:2}\t\t{1 if weights[0]*inputs[i][0] + weights[1]*inputs[i][1] +weights[2]*inputs[i][2] > 0 else -1:6}")
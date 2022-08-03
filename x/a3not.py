def step(X):
    return 1 if X > 0 else 0


w = float(input("Enter the weight        : "))
x = (1, 0)
expected = (0, 1)
learning_rate = float(input("Enter the learning rate : "))
bias = float(input("Enter the bias          : "))
epoch = 1
is_error = True

print("EPOCH     \tX     \tExpected Y     \tActual Y     \tError     \tW")
while is_error:
    is_error = False
    for i in range(2):
        weighted_sum = w * x[i] + bias
        Y = step(weighted_sum)
        error = expected[i] - Y
        if error:
            is_error = True
            w += learning_rate * error * x[i]
        print(f"{epoch:5}\t{x[i]:5}\t{expected[i]:14}\t{Y:12}\t{error:9}\t\t{w}")
    print()
    epoch += 1

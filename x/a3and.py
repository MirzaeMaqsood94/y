def step(X):
    return 1 if X > threshold else 0


w1, w2 = map(float, input("Enter the weights       : ").split())
x = ((0, 0), (0, 1), (1, 0), (1, 1))
expected = (0, 0, 0, 1)
learning_rate = float(input("Enter the learning rate : "))
threshold = float(input("Enter the threshold     : "))
epoch = 1
is_error = True

print("EPOCH     X1     X2     Expected Y     Actual Y     Error     W1     W2")
while is_error:
    is_error = False
    for i in range(4):
        weighted_sum = w1 * x[i][0] + w2 * x[i][1]
        Y = step(weighted_sum)
        error = expected[i] - Y
        if error:
            is_error = True
            w1 += learning_rate * error * x[i][0]
            w2 += learning_rate * error * x[i][1]
        print(f"{epoch:5}{x[i][0]:7}{x[i][1]:7}{expected[i]:15}{Y:13}{error:10}{w1:7}{w2:7}")
    print()
    epoch += 1

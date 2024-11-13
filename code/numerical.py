def euler_method(f, x0, y0, h, n):
    # Create lists to store x and y values
    x = [x0]
    y = [y0]

    # Euler algorithm
    for i in range(n):
        y.append(y[i] + h * f(x[i], y[i]))
        x.append(x[i] + h)

    return x, y


def modified_euler_method(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        # Predictor step
        y_predict = y_values[-1] + h * f(x_values[-1], y_values[-1])

        # Corrector step
        x_next = x_values[-1] + h
        y_correct = y_values[-1] + (h / 2) * (
            f(x_values[-1], y_values[-1]) + f(x_next, y_predict)
        )

        # Append the next values of x and y
        x_values.append(x_next)
        y_values.append(y_correct)

    return x_values, y_values


# The 4th-order Runge-Kutta method
def runge_kutta_4(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]

    # Iterate over each step
    for i in range(n):
        # Calculate intermediate slopes
        k1 = h * f(x_values[i], y_values[i])
        k2 = h * f(x_values[i] + h / 2, y_values[i] + k1 / 2)
        k3 = h * f(x_values[i] + h / 2, y_values[i] + k2 / 2)
        k4 = h * f(x_values[i] + h, y_values[i] + k3)

        # Compute the next value of y
        y_next = y_values[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x_values[i] + h

        # Append the next values of x and y
        x_values.append(x_next)
        y_values.append(y_next)

    return x_values, y_values

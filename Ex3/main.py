def multiply(x):
    return x + x


def double(x):
    return x * 2


def main():
    print(multiply(3))
    print((lambda x: x + x)(3))

    print(double(5))
    print((lambda x: x * 2)(5))


if __name__ == "__main__":
    main()

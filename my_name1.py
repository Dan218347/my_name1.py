def get_largest(largest, value):
    if largest is None:
        largest = value
    elif value > largest:
        largest = value
    return largest

def main():
    print("Welcome to my name1 program")
    largest = get_largest(7, 10)
    print("The largest value is {}".format(largest))

if __name__ == "__main__":
    main()

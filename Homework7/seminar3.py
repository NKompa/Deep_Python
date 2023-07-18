def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()


def write_to_file(results, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(results))


def calculate_result(numbers, names):
    results = []
    max_length = max(len(numbers), len(names))

    for i in range(max_length):
        num_line = numbers[i % len(numbers)].split('|')
        result = int(num_line[0]) * float(num_line[1])
        name_line = names[i % len(names)]

        if result < 0:
            results.append(f'{abs(result)}|{name_line.lower()}')
        else:
            results.append(f'{round(result)}|{name_line.upper()}')

    return results


def main():
    numbers = read_file('numbers.txt')
    names = read_file('names.txt')
    results = calculate_result(numbers, names)
    write_to_file(results, 'results.txt')


if __name__ == "__main__":
    main()
def save_unique_only(data_path, result_path):
    unique_lines = set()
    with open(data_path, 'r') as data:
        with open(result_path, 'w') as result:
            for line in data.readlines():
                unique_lines.add(line)
            result.writelines(list(unique_lines))

save_unique_only('homework-2/input.txt', 'homework-2/unique_output.txt')
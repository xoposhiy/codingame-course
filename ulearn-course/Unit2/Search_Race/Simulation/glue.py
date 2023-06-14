
result_filename = "result.py"
import_lines = set()
code = []
filenames = ["state.py", "estimate_task.py", "create_moves_task.py", "random_search_task.py", "main.py"]


def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("import"):
                import_lines.add(line)
            elif line.startswith("from"):
                module = line.split()[1] + ".py"
                if module not in filenames:
                    import_lines.add(line)
            else:
                code.append(line)


def main():
    for name in filenames:
        read_file(name)
    with open(result_filename, "w") as f:
        f.writelines(import_lines)
        f.writelines(code)


if __name__ == '__main__':
    main()


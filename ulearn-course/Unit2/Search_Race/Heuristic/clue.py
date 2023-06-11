
result_filename = "result.py"
import_lines = set()
code = []
filenames = ["heuristic.py", "heuristic2.py", "heuristic3.py", "heuristic4.py", "main.py"]


def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("import") or line.startswith("from"):
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


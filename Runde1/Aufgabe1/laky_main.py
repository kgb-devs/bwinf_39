INPUT_PATH = "input"


class Solver:
    def __init__(self):
        pass

    def main(self):
        self.read_inputs()

    def read_inputs(self):
        file_num = 0
        with open(f"{INPUT_PATH}/raetsel{file_num}.txt", "r", encoding="utf-8") as file:
            list_1 = file.readline().split()
            list_2 = file.readline().split()
            print(list_1)
            print(list_2)

if __name__ == '__main__':
    Solver().main()

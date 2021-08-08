INPUT_PATH = "input"


class Solver:
    def __init__(self):
        self.list_1 = None
        self.list_2 = None

    def main(self):
        self.read_inputs()

        # check for extra symbols
        for i in range(len(self.list_1)):
            if "," or "!" in self.list_1[i]:
                self.list_1[i] = self.list_1[i].replace(",", "")
                self.list_1[i] = self.list_1[i].replace("!", "")

        for i in range(len(self.list_1)):
            for char in self.list_1[i]:
                if char != "_":
                    print(self.list_1[i].index(char))

        print(self.list_1)
        print(self.list_2)

    def read_inputs(self):
        file_num = 0
        with open(f"{INPUT_PATH}/raetsel{file_num}.txt", "r", encoding="utf-8") as file:
            self.list_1 = file.readline().split()
            self.list_2 = file.readline().split()
            # print(self.list_1)
            # print(self.list_2)


if __name__ == '__main__':
    Solver().main()

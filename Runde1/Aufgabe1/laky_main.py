INPUT_PATH = "input"


class Solver:
    def __init__(self):
        self.list_1 = None
        self.list_2 = None
        self.list_result = []
        self.index_delete_1 = []
        self.index_delete_2 = []
        self.list_1_positions = []

    def main(self):
        self.read_inputs()

        # check for extra symbols
        for i in range(len(self.list_1)):
            if "," or "!" or "." in self.list_1[i]:
                self.list_1[i] = self.list_1[i].replace(",", "")
                self.list_1[i] = self.list_1[i].replace("!", "")
                self.list_1[i] = self.list_1[i].replace(".", "")

        for i in range(len(self.list_1)):
            for char in self.list_1[i]:
                if char != "_":
                    x = self.list_1[i].index(char)
                    # print(x)
                    for c in range(len(self.list_2)):
                        try:
                            if len(self.list_1[i]) == len(self.list_2[c]):
                                if self.list_2[c][x] == char:
                                    self.list_result.append(self.list_2[c])
                                    self.list_1[i] = ""
                                    self.list_2[c] = ""
                                    # print(f"found {self.list_1[i]} and {self.list_2[c]}")
                        except (ValueError, IndexError):
                            pass

        self.list_1_positions.extend(self.list_1)

        # print(self.list_1_positions)

        # print(self.list_1)

        while "" in self.list_1:
            self.list_1.remove("")

        while "" in self.list_2:
            self.list_2.remove("")

        for i in range(len(self.list_1)):
            for c in range(len(self.list_2)):
                if len(self.list_1[i]) == len(self.list_2[c]):
                    for n, item in enumerate(self.list_1_positions):
                        if len(item) == len(self.list_2[c]):
                            self.list_result.insert(n, self.list_2[c])

        # print(self.list_1)
        # print(self.list_2)
        # print(self.list_result)

        print(" ".join(str(x) for x in self.list_result))

    def read_inputs(self):
        file_num = 0
        with open(f"{INPUT_PATH}/raetsel{file_num}.txt", "r", encoding="utf-8") as file:
            self.list_1 = file.readline().split()
            self.list_2 = file.readline().split()
            # print(self.list_1)
            # print(self.list_2)


if __name__ == '__main__':
    Solver().main()

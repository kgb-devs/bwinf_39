INPUT_PATH = "input"


class Solver:
    def __init__(self):
        self.list_1 = None
        self.list_1_position = []
        self.list_2 = None
        self.list_2_position = []
        self.result = []

    def main(self):
        self.read_inputs()

        # Sonderzeichen?
        for i in range(len(self.list_1)):
            if "," or "!" in self.list_1[i]:
                self.list_1[i] = self.list_1[i].replace(",", "")
                self.list_1[i] = self.list_1[i].replace("!", "")

        print(self.list_1)
        print(self.list_2)

        for i in range(len(self.list_1)):
            for char in self.list_1[i]:
                if char != "_":
                    x = self.list_1[i].index(char)
                    #print(x)
                    #print(char)
                    for c in range(len(self.list_2)):
                        try:
                            if len(self.list_2[c]) == len(self.list_1[i]):
                                if self.list_2[c][x] == char:
                                    #print(f" {self.list_1[i]} gehört zu: {self.list_2[c]}")
                                    self.result.insert(i, self.list_2[c])
                                    self.list_1[i] = ""
                                    self.list_2[c] = ""

                        except:
                            pass

        self.list_1_position.extend(self.list_1)
        self.list_2_position.extend(self.list_2)

        while "" in self.list_1:
            self.list_1.remove("")
        while "" in self.list_2:
            self.list_2.remove("")

        #print(self.list_1)
        #print(self.list_2)
        #print(self.list_1_position)
        #print(self.list_2_position)
        #print(self.list_result)

        for i in range(len(self.list_1)):
            for c in range(len(self.list_2)):
                try:
                    if len(self.list_2[c]) == len(self.list_1[i]):
                            #print(f" {self.list_1[i]} gehört zu: {self.list_2[c]}")
                            for j in range(len(self.list_1_position)):
                                try:
                                    if len(self.list_1_position[j]) == len(self.list_1[i]):
                                        self.result.insert(j, self.list_2[c])
                                except:
                                    pass


                except:
                    pass
        #print(self.list_1)
        #print(self.list_2)
        #print(self.result)
        print(" ".join(str(x) for x in self.result))

    # öffnet die Datei
    def read_inputs(self):
        file_num = 0  # reatselnummer
        with open(f"{INPUT_PATH}/raetsel{file_num}.txt", "r", encoding="utf-8") as file:
            self.list_1 = file.readline().split()
            self.list_2 = file.readline().split()
            # print(self.list_1)
            # print(self.list_2)


if __name__ == '__main__':
    Solver().main()

class Fastener:
    def __init__(self, title, size1_label, size2_label, formula, C1, C2):
        self.title = title
        self.size1_label = size1_label
        self.size2_label = size2_label
        self.formula = formula
        self.C1 = C1
        self.C2 = C2


class Material:
    def __init__(self, title, size1_label, size2_label, formula, C1, C2):
        self.title = title
        self.size1_label = size1_label
        self.size2_label = size2_label
        self.formula = formula
        self.C1 = C1
        self.C2 = C2


class ProcessMultiplier:
    def __init__(self, title, value):
        self.title = title
        self.value = value


class Process:
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost


class Tool:
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost


def main():
    pass


if __name__ == "__main__":
    main()

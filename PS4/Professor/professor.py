import random


def main():
    print(generate_integer(get_level()))


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in (1, 2, 3):
                return level


def generate_integer(level):
    number = 10
    score = 0

    while number != 0:
        # Level 1
        if level == 1:
            number = number - 1

            level1_a = random.randint(0, 9)
            level1_b = random.randint(0, 9)
            ans_1 = level1_a + level1_b

            try:
                # First incorrect answer
                input_ans = int(input(f"{level1_a} + {level1_b} = "))
                if input_ans != ans_1:
                    print("EEE")

                    input_ans = int(input(f"{level1_a} + {level1_b} = "))
                    if input_ans != ans_1:          # Second incorrect answer
                        print("EEE")

                        input_ans = int(input(f"{level1_a} + {level1_b} = "))
                        if input_ans != ans_1:                      # Third incorrect answer
                            print(f"{level1_a} + {level1_b} = {ans_1}")

                else:
                    score += 1
                    pass
            except ValueError:
                print("EEE")

                input_ans = int(input(f"{level1_a} + {level1_b} = "))
                if input_ans != ans_1:              # Second incorrect answer
                    print("EEE")

                    input_ans = int(input(f"{level1_a} + {level1_b} = "))
                    if input_ans != ans_1:                          # Third incorrect answer
                        print(f"{level1_a} + {level1_b} = {ans_1}")

        # Level 2
        elif level == 2:
            number = number - 1

            level2_a = random.randint(10, 99)
            level2_b = random.randint(10, 99)
            ans_2 = level2_a + level2_b

            try:
                # First incorrect answer
                input_ans = int(input(f"{level2_a} + {level2_b} = "))
                if input_ans != ans_2:
                    print("EEE")

                    input_ans = int(input(f"{level2_a} + {level2_b} = "))
                    if input_ans != ans_2:          # Second incorrect answer
                        print("EEE")

                        input_ans = int(input(f"{level2_a} + {level2_b} = "))
                        if input_ans != ans_2:                      # Third incorrect answer
                            print(f"{level2_a} + {level2_b} = {ans_2}")

                else:
                    score += 1
                    pass
            except ValueError:
                print("EEE")

                input_ans = int(input(f"{level2_a} + {level2_b} = "))
                if input_ans != ans_2:              # Second incorrect answer
                    print("EEE")

                    input_ans = int(input(f"{level2_a} + {level2_b} = "))
                    if input_ans != ans_2:                          # Third incorrect answer
                        print(f"{level2_a} + {level2_b} = {ans_2}")

        # Level 3
        elif level == 3:
            number = number - 1

            level3_a = random.randint(100, 999)
            level3_b = random.randint(100, 999)
            ans_3 = level3_a + level3_b

            try:
                # First incorrect answer
                input_ans = int(input(f"{level3_a} + {level3_b} = "))
                if input_ans != ans_3:
                    print("EEE")

                    input_ans = int(input(f"{level3_a} + {level3_b} = "))
                    if input_ans != ans_3:          # Second incorrect answer
                        print("EEE")

                        input_ans = int(input(f"{level3_a} + {level3_b} = "))
                        if input_ans != ans_3:                      # Third incorrect answer
                            print(f"{level3_a} + {level3_b} = {ans_3}")

                else:
                    score += 1
                    pass
            except ValueError:
                print("EEE")

                input_ans = int(input(f"{level3_a} + {level3_b} = "))
                if input_ans != ans_3:              # Second incorrect answer
                    print("EEE")

                    input_ans = int(input(f"{level3_a} + {level3_b} = "))
                    if input_ans != ans_3:                          # Third incorrect answer
                        print(f"{level3_a} + {level3_b} = {ans_3}")

    return (f"Score = {score}")


if __name__ == "__main__":
    main()


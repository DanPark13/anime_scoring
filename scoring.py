# Python Script for Rating Anime because I have no life

story, characters, art, sound, enjoyment = [0.0 for _ in range(5)]

story = float(input("Input Story Score: "))
characters = float(input("Input Characters Score: "))
art = float(input("Input Art Score: "))
sound = float(input("Input Sound Score: "))
enjoyment = float(input("Input Enjoyment Score: "))


def calculate_score(s, c, a, h, e):
    return ((s + c) * 0.35) + ((a + h) * 0.025) + (e * 0.25)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f"Your Rating is {calculate_score(story, characters, art, sound, enjoyment)}")

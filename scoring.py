# Python Script for Rating Anime because I have no life

story = float(input("Input Story Score: "))
characters = float(input("Input Characters Score: "))
art = float(input("Input Art Score: "))
sound = float(input("Input Sound Score: "))
enjoyment = float(input("Input Enjoyment Score: "))


def calculate_score(s, c, a, h, e):
    return ((s + c) * 0.35) + ((a + h) * 0.025) + (e * 0.25)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    final_score = calculate_score(story, characters, art, sound, enjoyment)
    print(f"Story: {int(story)} | Characters: {int(characters)} "
          f"| Art: {int(art)} | Sound: {int(sound)} | Enjoyment: {int(enjoyment)}")
    print(f"Your Rating is {final_score} which rounds to "
          f"{round(final_score,1)}")

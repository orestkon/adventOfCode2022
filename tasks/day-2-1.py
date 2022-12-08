rules1 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

rules2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

def readInput():
    f = open("./inputs/day-2-1.txt")
    return f.read().splitlines()

def scorePerRound(lines):
    score = []
    for line in lines:
        # Uncomment the line below for first part
        # score.append(rules1.get(line))
        # Uncomment the line below for second part
        score.append(rules2.get(line))
    return score

if __name__ == '__main__':
    lines = readInput()
    score = scorePerRound(lines)
    print(sum(score))
def readInput():
    f = open("./inputs/day-1-1.txt")
    return f.readlines()

def caloriesPerElf(lines):
    calories = [0]
    count = 0
    for line in lines:
        if line == '\n':
            count = count + 1
            calories.append(0)
        else:
            calories[count] += int(line)
    return calories
    

if __name__ == '__main__':
    lines = readInput()
    calories = caloriesPerElf(lines)
    sortedCalories = sorted(calories, reverse=True)
    print(sortedCalories[0]+sortedCalories[1]+sortedCalories[2])
    
def readInput():
    f = open("./inputs/day-1-1.txt")
    return f.readlines()

def logic(lines):
    calories = [0]
    count = 0
    for line in lines:
        if line == '\n':
            count = count  + 1
            calories.append(0)
            # print("Empty line")
        else:
            calories[count] += int(line)
            # print("Number")
    return calories
    

if __name__ == '__main__':
    lines = readInput()
    calories = logic(lines)
    print(max(calories))
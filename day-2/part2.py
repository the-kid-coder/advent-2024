# This is a problem from the 2024 Advent of Code calendar.
# Part 2 of Day 2

reports = []

# The goal of this function is to populate the two lists for this exercise
def input_lists():
    with open("input.txt",'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            
            reports.append(line.split(" "))

def checkReport(report):
    if int(report[0]) > int(report[1]):
        return checkDecreasing(report)
    elif int(report[0]) < int(report[1]):
        return checkIncreasing(report)


def checkDecreasing(report):
    for i in range(len(report) - 1):
        current = int(report[i])
        next = int(report[i+1])
        if current > next:
            if (abs(current - next) > 3):
                return 0
        elif current == next:
            return 0
        else:
            return 0
    
    return 1


def checkIncreasing(report):
    for i in range(len(report) - 1):
        current = int(report[i])
        next = int(report[i+1])
        if current < next:
            if (abs(current - next) > 3):
                return 0
        else:
            return 0
    
    return 1

def main():
    input_lists()
    safe_reports = 0
    
    for report in reports:
        if checkReport(report) == 1:
            safe_reports += 1
        else:
            for i in range(len(report)):
                temp_report = report.copy()
                temp_report.pop(i)
                if checkReport(temp_report) == 1:
                    safe_reports += 1
                    break
    
    print(safe_reports)

main()

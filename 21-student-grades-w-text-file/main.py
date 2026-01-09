def calculate_grade(line):
    # Remove newline character
    line = line[:-1]

    parts = line.split(",")
    name = parts[0]
    exam1 = int(parts[1])
    exam2 = int(parts[2])
    exam3 = int(parts[3])

    final_grade = exam1 * 0.3 + exam2 * 0.3 + exam3 * 0.4

    if final_grade >= 90:
        letter = "AA"
    elif final_grade >= 85:
        letter = "BA"
    elif final_grade >= 80:
        letter = "BB"
    elif final_grade >= 75:
        letter = "CB"
    elif final_grade >= 70:
        letter = "CC"
    elif final_grade >= 65:
        letter = "DC"
    elif final_grade >= 55:
        letter = "DD"
    else:
        letter = "FF"

    return f"{name} -----------------------> {letter}\n"


with open("student-grades.txt", "r", encoding="utf-8") as file:
    results = []

    for line in file:
        results.append(calculate_grade(line))

    print(results)

    with open("results.txt", "a", encoding="utf-8") as output_file:
        for result in results:
            output_file.write(result)

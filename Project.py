'''
Group Members: Rohin Kalra, Muhammad Kaif Imran Malik, Jaquoub Alsharrah, Emily Hartman
Full Name: 
ID:
Date: 
Filename: 
Purpose: Get a filename from a config.txt file and write all information in that file to a csv file.
'''

import matplotlib.pyplot as plt

def create_2d_array(file):
    # File must be of str type, readable, and have commas separating elements
    # Returns a 2D array of the information presented in the full
    readfile = open(file, "r")
    lst_2d = []
    for line in readfile:
        line = line.split(",") # Convert line into a list
        lst_1d = []
        for idx in range(len(line)):
            if idx < 2:
                lst_1d += [line[idx]]
            else:
                lst_1d += [int(line[idx])]
        lst_2d += [lst_1d]
    return lst_2d

def empty_file(file):
    # File must be of str type
    # Will empty a file, or create an empty file if none exists in that name
    writefile = open(file, "w")
    writefile.close()

def write_column_headers(T, L, Q, A, P, B, file):
    # Takes the  number of each assignment and the file
    # Writes the column headers and returns a list of the assignments
    assignments = []
    writefile = open(file, "a")
    writefile.write("Student Name, Student ID,")
    if T != 0:
        for x in range(1, int(T) + 1):
            string = "T." + str(x) + ","
            writefile.write(string)
            assignments += [string]
    if L != 0:
        for x in range(1, int(L) + 1):
            string = "L." + str(x) + ","
            writefile.write(string)
            assignments += [string]
    if Q != 0:
        for x in range(1, int(Q) + 1):
            string = "Q." + str(x) + ","
            writefile.write(string)
            assignments += [string]
    if A != 0:
        for x in range(1, int(A) + 1):
            string = "A." + str(x) + ","
            writefile.write(string)
            assignments += [string]
    if P != 0:
            writefile.write("P,")
            assignments += [string]
    if B != 0:
            writefile.write("B,")
            assignments += [string]
    writefile.write("T.X Avg, L.X Avg, Q.X Avg, A.X Avg, Grade")
    writefile.write("\n\n")
    writefile.close()
    return assignments

def calculate_student_averages(student, start_column, num, drops, max_points):
    # Takes the student, the column to start taking information from, the number of that particular assignment, drops, and maximum points
    # Returns the student percent

    # Add all assessments to a list
    all_assessments = []
    for i in range(start_column, start_column + int(num)):
        all_assessments += [int(student[i])]
    # Sort the list
    sorted_assessments_lst = []
    for x in all_assessments:
        sorted_assessments_lst += [int(x)]
    for i in range(1, len(sorted_assessments_lst)):
        key = sorted_assessments_lst[i]
        j = i - 1
        while j >= 0 and key < sorted_assessments_lst[j]:
            sorted_assessments_lst[j+1] = sorted_assessments_lst[j]
            j = j - 1
            sorted_assessments_lst[j+1] = key
    # Add only the top necessary values
    top_assessments = []
    for i in range(num - 1, drops * -1 - 1, -1):
        top_assessments += [sorted_assessments_lst[i]]
    # Calculate Average
    sum = 0
    num_of_included_assessments = num + drops
    for value in top_assessments:
        sum += value
    if num_of_included_assessments == 0:
        average_score = 0
    else:
        average_score = sum / num_of_included_assessments
    percent = average_score / max_points
    # Add average to student list
    student += [percent]
    return percent

def write_student_information(gradebook, file):
    # Gradebook should be a 2D list, file should be of str type
    # Writes all elements in gradebook to given file
    writefile = open(file, "a")
    for i in range(len(gradebook)):
        for j in range(len(gradebook[i])):
            if j < 2:
                writefile.write(gradebook[i][j]) 
                writefile.write(",")
            else:
                writefile.write(str(gradebook[i][j]))
                writefile.write(",")
        writefile.write("\n\n")
    writefile.close()

def setup_column_averages(file):
    # File needs to be of str type
    # Writes "Class, Averages,"to the given file
    writefile = open(file, "a")
    writefile.write("Class, Averages,")
    writefile.close()

def calculate_column_averages(gradebook, j, file):
    # Gradebook should be a 2D list, j should be an int within len(gradebook), and file should be of str type
    # Writes the averages of each column to the given file
    total = 0
    num_of_students = len(gradebook)
    for student in gradebook:
        total += int(student[j])
    average = str(total / num_of_students)
    writefile = open(file, "a") 
    writefile.write(average)
    writefile.write(",")
    writefile.close()
    return average

def get_grade_weights(secondline):
    # Takes a list containing information regarding the weights of grades
    # Returns a list of grade weights in a specific order
    for val in secondline:
        weight = int(val[1:])
        if val[0] == "T":
            T_weight = weight
        elif val[0] == "L":
            L_weight = weight
        elif val[0] == "Q":
            Q_weight = weight      
        elif val[0] == "A":
            A_weight = weight
        elif val[0] == "P":
            P_weight = weight
        elif val[0] == "B":
            B_weight = weight
    return [T_weight, L_weight, Q_weight, A_weight, P_weight, B_weight]

def get_grade_distribution(thirdline):
    # Takes a list that contains information regarding the grade distribution
    # Will return a list containing grade distribution in order from A to F
    for val in thirdline:
        if val[:2] == "A-":
            A_minus_min = float(val[2:4])
            A_minus_max = float(val[5:])
        elif val[0] == "A":
            A_min = float(val[1:3])
            A_max = 100
        elif val[:2] == "B+":
            B_plus_min = float(val[2:4])
            B_plus_max = float(val[5:])
        elif val[:2] == "B-":
            B_minus_min = float(val[2:4])
            B_minus_max = float(val[5:])
        elif val[0] == "B":
            B_min = float(val[1:3])
            B_max = float(val[4:])
        elif val[:2] == "C+":
            C_plus_min = float(val[2:4])
            C_plus_max = float(val[5:])
        elif val[:2] == "C-":
            C_minus_min = float(val[2:4])
            C_minus_max = float(val[5:])
        elif val[0] == "C":
            C_min = float(val[1:3])
            C_max = float(val[4:])
        elif val[:2] == "D+":
            D_plus_min = float(val[2:4])
            D_plus_max = float(val[5:])
        elif val[:2] == "D-":
            D_minus_min = float(val[2:4])
            D_minus_max = float(val[5:])
        elif val[0] == "D":
            D_min = float(val[1:3])
            D_max = float(val[4:])
        elif val[0] == "F":
            F_min = 0
            F_max = float(val[2:])
    return [A_max, A_min, A_minus_max, A_minus_min, B_plus_max, B_plus_min, B_max, B_min,\
            B_minus_max, B_minus_min, C_plus_max, C_plus_min, C_max, C_min, C_minus_max,\
            C_minus_min, D_plus_max, D_plus_min, D_max, D_min, D_minus_max, D_minus_min, F_max, F_min]

def calculate_final_grade(T, L, Q, A, P, B, weights, gd):
    # Takes student grade percents, the list of grade weights of the assignemnts, and the grade requirements
    # Returns the students letter grade
    grade = T * weights[0] + L * weights[1] + Q * weights[2] + A * weights[3] + P * weights[4] + B * weights[5] 
    if grade <= gd[0] and grade >= gd[1]:
        letter_grade = "A"
    elif grade <= gd[2] and grade >= gd[3]:
        letter_grade = "A-"
    elif grade <= gd[4] and grade >= gd[5]:
        letter_grade = "B+"
    elif grade <= gd[6] and grade >= gd[7]:
        letter_grade = "B"
    elif grade <= gd[8] and grade >= gd[9]:
        letter_grade = "B-"
    elif grade <= gd[10] and grade >= gd[11]:
        letter_grade = "C+"
    elif grade <= gd[12] and grade >= gd[13]:
        letter_grade = "C"
    elif grade <= gd[14] and grade >= gd[15]:
        letter_grade = "C-"
    elif grade <= gd[16] and grade >= gd[17]:
        letter_grade = "D+"
    elif grade <= gd[18] and grade >= gd[19]:
        letter_grade = "D"
    elif grade <= gd[20] and grade >= gd[21]:
        letter_grade = "D-"
    elif grade <= gd[22] and grade >= gd[23]:
        letter_grade = "F"
    return letter_grade

def main():
    configfile = open("config.txt", "r") 
    firstline = configfile.readline().split(",")
    secondline = configfile.readline().split(" ")
    thirdline = configfile.readline().split(",")
    configfile.close()
    writefile = "gradebook.csv" 
    empty_file(writefile)
    readfile = firstline[0]
    gradebook = create_2d_array(readfile) 
    weights = get_grade_weights(secondline)
    grade_distribution = get_grade_distribution(thirdline)
    for student in gradebook:
        start_column = 2
        TX_grade = calculate_student_averages(student, start_column, int(firstline[1]), int(firstline[2]), int(firstline[3])) # T.X Assessment Student Average 
        start_column += int(firstline[1])
        LX_grade = calculate_student_averages(student, start_column, int(firstline[4]), int(firstline[5]), int(firstline[6])) # L.X Assessment Student Average 
        start_column += int(firstline[4])
        QX_grade = calculate_student_averages(student, start_column, int(firstline[7]), int(firstline[8]), int(firstline[9])) # Q.X Assessment Student Average 
        start_column += int(firstline[7])
        AX_grade = calculate_student_averages(student, start_column, int(firstline[10]), int(firstline[11]), int(firstline[12])) # A.X Assessment Student Average 
        start_column += int(firstline[10])
        P_grade = student[start_column] / int(firstline[15]) # P Score 
        start_column += int(firstline[13])
        B_grade = student[start_column] / int(firstline[18]) # B Score 
        letter_grade = calculate_final_grade(TX_grade, LX_grade, QX_grade, AX_grade, P_grade, B_grade, weights, grade_distribution)
        student += [letter_grade]

    # Writing the information to file
    assignments = write_column_headers(firstline[1], firstline[4], firstline[7], firstline[10], firstline[13], firstline[16], writefile) # Give number of T, L, Q, A, P, B Columns, get list of assignment names
    write_student_information(gradebook, writefile)
    setup_column_averages(writefile)
    col_avg_lst = [] # List of column averages
    for j in range(2, len(gradebook[0]) - 5):
        average = calculate_column_averages(gradebook, j, writefile)
        col_avg_lst += [int(float(average))]

    # Histogram (Bar Graph)
    x_axis = assignments
    y_axis = col_avg_lst
    plt.bar(x_axis, y_axis)
    plt.title("Grades")
    plt.xlabel("Assignment")
    plt.ylabel("Average Score")
    plt.show()

main()

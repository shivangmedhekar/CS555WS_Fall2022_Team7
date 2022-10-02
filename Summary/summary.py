def summary(individuals_table, families_table, logs):

    print("Indiviudals")
    print(individuals_table)

    print("Families")
    print(families_table)

    print("\nUser Story Logs")
    for log in logs:
        print(log)

    with open("output.txt", "w") as output_file:

        
        output_file.write("Indiviudals\n")
        output_file.write(str(individuals_table))


        output_file.write("\nFamilies\n")
        output_file.write(str(families_table))
        
        output_file.write("\n\nUser Stories Logs\n")
        for log in logs:
            output_file.write(log)
            output_file.write("\n")
            
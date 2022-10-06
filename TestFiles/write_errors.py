def write_errors(error):
    with open("output.txt", "a") as output_file:
        print(error)
        output_file.write(error)
        output_file.write("\n")
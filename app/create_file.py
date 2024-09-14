import sys
import os
import datetime


def create_directory(directory: str) -> None:
    if not os.path.exists(directory):
        os.mkdir(directory)


def create_and_write_into_file(file_name: str) -> None:
    with open(file_name, "a") as source_file:
        current_date = datetime.datetime.now()
        source_file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            source_file.write(f"{line_number} {new_line}\n")
            line_number += 1
        source_file.write("\n")


commands = sys.argv
if commands[1] == "-d":
    path = commands[2]
    create_directory(path)
    for i in range(3, len(commands)):
        if commands[i] != "-f":
            path = os.path.join(path, commands[i])
            create_directory(path)
        elif commands[i] == "-f":
            path = os.path.join(path, commands[i + 1])
            create_and_write_into_file(path)
            break
elif commands[1] == "-f":
    create_and_write_into_file(commands[2])

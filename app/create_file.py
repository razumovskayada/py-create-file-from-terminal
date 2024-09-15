import sys
import os
import datetime


def create_and_write_into_file(file_name: str) -> None:
    current_date = datetime.datetime.now()
    text = []
    line_number = 1
    while True:
        new_line = input("Enter content line: ")
        if new_line == "stop":
            break
        text.append(f"{line_number} {new_line}\n")
        line_number += 1
    with open(file_name, "a") as source_file:
        source_file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        source_file.writelines(text)
        source_file.write("\n")


def handle_command() -> None:
    commands = sys.argv
    if commands[1] == "-d":
        path = commands[2]
        os.makedirs(path, exist_ok=True)
        for i in range(3, len(commands)):
            if commands[i] == "-f":
                path = os.path.join(path, commands[i + 1])
                create_and_write_into_file(path)
                break
            path = os.path.join(path, commands[i])
            os.makedirs(path, exist_ok=True)
    elif commands[1] == "-f":
        if len(commands) > 3:
            path = commands[4]
            os.makedirs(path, exist_ok=True)
            for i in range(5, len(commands)):
                path = os.path.join(path, commands[i])
                os.makedirs(path, exist_ok=True)
            path = os.path.join(path, commands[2])
            create_and_write_into_file(path)
        else:
            create_and_write_into_file(commands[2])


if __name__ == "__main__":
    handle_command()

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess



def find_all_files(start_path: str) -> list[tuple[str, list[str], list[str]]]:
    """
    :param start_path: path where we need to start to look at
    :return : a list of 3-tuples where the first item is the root directory,
              the second item is all the child directories, and the third item is all the files
    """
    result = []
    for dirs, subdirs, files in os.walk(start_path):
        result.append((dirs, subdirs, files))
    return result



def open_powershell() -> subprocess.Popen:
    """
    Opens a new PowerShell session in the background.
    :return: the subprocess.Popen object representing the PowerShell process
    """
    powershell_process = subprocess.Popen(
        ["powershell", "-NoExit", "-Command", "Start-Transcript -Path output.txt"], stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    return powershell_process



def send_powershell_command(process: subprocess.Popen, cmd: str):
    """
    Sends a command to an existing PowerShell session.
    :param process: the subprocess.Popen object representing the PowerShell process
    :param cmd: the command to send
    """
    process.stdin.write(cmd + '\n')
    process.stdin.flush()


def close_powershell(process: subprocess.Popen):
    """
    Closes the PowerShell session and stops the transcript.
    :param process: the subprocess.Popen object representing the PowerShell process
    """
    process.stdin.write('Stop-Transcript\n')
    process.stdin.flush()
    process.stdin.write('exit\n')
    process.stdin.flush()
    process.communicate()  # Wait for PowerShell to exit and clean up


def main():
    ps_process = open_powershell()  # Start the PowerShell to send the data

    data = find_all_files('D:\\dnd')
    for dirs, subdirs, files in data:
        for subdir in subdirs:
            subdir_path = os.path.join(dirs, subdir)
            send_powershell_command(ps_process, f'mkdir {subdir_path}')
        for file in files:
            file_path = os.path.join(dirs, file)
            send_powershell_command(ps_process, f'mput {file_path}')







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

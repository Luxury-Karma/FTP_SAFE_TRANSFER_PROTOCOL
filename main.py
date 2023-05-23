# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess



def find_all_files(start_path: str) -> list[list[str]]:
    """
    :param start_path: path where we need to start to look at
    :return : a array of list where in each list the 0 is the root directory, 1 are all the child directory and 2 are all the files
    """
    dirs, files = os.walk(start_path)
    return [dirs, files]


import subprocess

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
    send_powershell_command(ps_process, 'ls')
    files = find_all_files('D:\\dnd')






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

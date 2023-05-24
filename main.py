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


# Create Directory
def push_directory(data, ps_process, linux_dir: str):
    #send_powershell_command(f'cd {linux_dir}')  # Go in the linux directory to add those files and dires
    for dirs, subdirs, files in data:
        live_directory = dirs.split('\\')
        live_directory: str = live_directory[len(live_directory)-1]
        #send_powershell_command(f'lcd {dirs}')  # make all of the subdirectories
        #send_powershell_command(ps_process, f'cd .\\{live_directory}')  #  place in the correct directory in the linux server
        send_powershell_command(ps_process,f'mkdir {live_directory}')
        for subdir in subdirs:
            send_powershell_command(ps_process, f'mkdir {subdir}')  # Create all the directories

        #send_powershell_command(f'lcd {dirs}')  # Swictch the main computer to the directory of the file
        for file in files:
            file_path = os.path.join(dirs, file)
            send_powershell_command(ps_process, f'mput {file}')  # send the files


def ssh_connection(ps_process: subprocess, ipaddress: str, account: str, password: str):
    send_powershell_command(ps_process,f'ftp {ipaddress}')
    send_powershell_command(ps_process, f'{account}')
    send_powershell_command(ps_process, f'{password}')


def main(moving_directory: str):

    ps_process = open_powershell()  # Start the PowerShell to send the data
    data = find_all_files(moving_directory)
    linux_dir = moving_directory.split('\\')
    linux_dir = linux_dir[len(linux_dir)-1]
    push_directory(data, ps_process, linux_dir)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('D:\\dnd')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

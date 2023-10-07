'''
decrypt.py

The file is made to decrypt the password of a PDF file. 
Users must run the script from the command prompt or PowerShell 
as `python path/to/script/decrypt.py` or `python decrypt.py` if 
the shell was run from the same place as `decrypt.py`.

'''

import sys
import os
import platform
import getpass
import time


def check_internet_connection():
    '''
    Check if the script has internet connectivity.

    Returns:
        bool: True if connected, False otherwise.
    '''
    try:
        # Redirect output to null
        response = os.system("ping 8.8.8.8 > nul 2>&1")
        return response == 0
    except Exception as e:
        print(f"Error checking internet connection: {e}")
        return False


def install_required_modules():
    '''
    Install required Python modules.

    Raises:
        SystemExit: If the required modules cannot be installed.
    '''
    required_modules = ['PyPDF2', 'PyCryptodome']
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"\033[0;36m{module} module not found. Installing...")
            os.system(f"pip install {module}")
        else:
            print(f"\033[0;33m{module} module already installed.")


def generate_password(name):
    '''
    Generate a password for decrypting a PDF.

    Args:
        name (str): The user's name.

    Returns:
        str: The generated password.
    '''
    return f'reader={name.lower()}.'


def decrypt_pdf(input_path, output_path, name):
    '''
    Decrypt a PDF file.

    Args:
        input_path (str): The path to the encrypted PDF file.
        output_path (str): The path to save the decrypted PDF file.
        name (str): The user's name.

    Raises:
        SystemExit: If required modules are not found.
    '''
    password = generate_password(name)

    try:
        from PyPDF2 import PdfReader, PdfWriter
    except ImportError:
        print("\033[31mError: Required module PyPDF2 not found. Please install it manually using 'pip install PyPDF2'.\033[0m")
        sys.exit(1)

    try:
        from Crypto.Cipher import AES
    except ImportError:
        print("\033[31mError: Required module pycryptodome not found. Please install it manually using 'pip install pycryptodome'.\033[0m")
        sys.exit(1)

    with open(input_path, 'rb') as file:
        pdf_reader = PdfReader(file)

        if pdf_reader.is_encrypted:
            if pdf_reader.decrypt(password):
                with open(output_path, 'wb') as output_file:
                    pdf_writer = PdfWriter()
                    for page in pdf_reader.pages:
                        pdf_writer.add_page(page)
                    pdf_writer.write(output_file)
                print(
                    "\033[32mPDF decrypted successfully.\033[0m Decrypted file saved as \033[32m", output_path, "\033[0m")
                os.system(f'start {output_path}' if os.name ==
                          'nt' else f'xdg-open {output_path}')
                time.sleep(1)
                os.remove(f'{output_path}')
            else:
                print(
                    "\033[31mIncorrect name. Unable to decrypt the PDF.\033[0m")
        else:
            print("\033[31mThe PDF is not encrypted. No need to decrypt.\033[0m")


def print_welcome_message():
    '''
    Print a welcome message and device information.
    '''
    internet_status = "Connected" if check_internet_connection() else "No Connection"

    print("""
\033[31m===============================================\033[0m
\033[33m               Welcome to PDF Decryptor\033[0m
\033[34m  ESUBALEW  _            __ _ _      
\033[34m / ___|| |_   ___  / _(_) | ___ 
\033[34m \___ \| | | |  _ \| |_| | |/ _ \\
\033[34m  ___) | | | | |_) |  _| | |  __/
\033[34m |____/|_| |_|  __/|_| |_|_|\___|
\033[31m===============================================\033[0m
""")

    print("\033[36mDevice Information:\033[0m")
    print(f"\033[36m  OS:\033[0m {platform.system()} {platform.version()}")
    print(f"\033[36m  Python Version:\033[0m {platform.python_version()}")
    print(
        f"\033[36m  Script Running on:\033[0m {platform.machine()} {platform.architecture()}")
    print(f"\033[36m  Device Name:\033[0m {platform.node()}")
    print(
        f"\033[36m  Internet Status:\033[0m [\033[32m{internet_status}\033[0m]")
    print("\033[36m===============================================\033[0m")
    print("\033[34mTo use this script, follow these steps:\033[0m")
    print(
        "\033[34m  1. Provide the encrypted PDF file as a command-line argument.\033[0m")
    print("\033[34m  2. Enter your name when prompted.\033[0m")
    print(
        "\033[34m  3. The script will decrypt the PDF and open the decrypted file.\033[0m")
    print("\033[34m===============================================\033[0m")


def main():
    '''
    Main function to run the PDF decryption script.
    '''
    install_required_modules()
    print_welcome_message()

    try:
        from PyPDF2 import PdfReader, PdfWriter
    except ImportError:
        print("\033[31mError: Required module PyPDF2 not found. Please install it manually using 'pip install PyPDF2'.\033[0m")
        sys.exit(1)

    try:
        from Crypto.Cipher import AES
    except ImportError:
        print("\033[31mError: Required module pycryptodome not found. Please install it manually using 'pip install pycryptodome'.\033[0m")
        sys.exit(1)

    if len(sys.argv) != 2:
        print("\033[31mUsage: python decrypt.py [filename.pdf] please add the file name after python script name\033[0m")
        sys.exit(1)

    input_pdf_path = sys.argv[1]

    if not os.path.exists(input_pdf_path):
        print("\033[31mError: The provided file does not exist.\033[0m")
        sys.exit(1)

    user_name = getpass.getpass(
        prompt='\033[1;33mEnter your name[Don\'t worry if what you enter is invisible]:\033[0m ')

    output_pdf_path = f'decrypted_{os.path.basename(input_pdf_path)}'

    decrypt_pdf(input_pdf_path, output_pdf_path, user_name)


if __name__ == "__main__":
    main()

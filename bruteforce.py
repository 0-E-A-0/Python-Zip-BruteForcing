'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        # Attempt to extract all files from the ZIP archive using the provided password
        zf_handle.extractall(pwd=password.encode())
        # If successful, print a message indicating that the password was found
        print(f"[+] Password found: {password}")
        return True
    except Exception as e:

    # Incorrect password or other error occured     
        print(f"[-] Error: {e}")
        return False

#
# Define the main function for the bruteforce attack
def main():
    # Print a message indicating the beginning of the bruteforce process
    print("[+] Beginning bruteforce ")

    # Open the encrypted ZIP file and declear it in zf variable
    with ZipFile('enc.zip') as zf:
        # Open the file containing a list of passwords to try (i.e. rockyou.txt)
        with open('rockyou.txt', 'r') as f:

            # Iterate through password entries in rockyou.txt
            for password in f:
                password = password.strip() # Remove leadin/trailing whitespace from the password list

            # Attempt to extract the ZIP file using the current password by calling the function
                if attempt_extract(zf, password):
                    return # Exit loop if password found and terminate the script.

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
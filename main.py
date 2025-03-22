import os

def main():
    while True:
        print("\n=== Telegram Scraper Menu ===")
        print("1. Run Manager")
        print("2. Run Scraper")
        print("3. Run Another Script")  # Add more options if needed
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            os.system("python manager.py")
        elif choice == "2":
            os.system("python scraper.py")
        elif choice == "3":
            script_name = input("Enter script name (e.g., example.py): ")
            os.system(f"python {script_name}")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

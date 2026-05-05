import time
import sys
import os

# Typing animation
def type_text(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Fake loading bar
def loading(text="Loading", duration=2):
    type_text(text)
    for i in range(20):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(duration / 20)
    print("\n")

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Boot sequence
def boot():
    clear()
    type_text("Initializing system...", 0.03)
    loading("Booting Dev Hub")
    type_text("Access granted.\n", 0.03)
    time.sleep(0.5)

# Sections
def show_about():
    type_text("\n[ ABOUT ]", 0.04)
    type_text("Hello, I'm a beginner developer exploring Python and web development.")
    type_text("Building projects and improving every day.\n")

def show_projects():
    type_text("\n[ PROJECTS ]", 0.04)
    type_text("1. Portfolio Website (HTML)")
    type_text("2. Python Mini Games")
    type_text("3. More coming soon...\n")

def show_contact():
    type_text("\n[ CONTACT ]", 0.04)
    type_text("GitHub: github.com/AdhyanChettri-boop")
    type_text("Email: adhyanchettri83@gmail.com\n")

def help_menu():
    type_text("\nAvailable commands:")
    type_text("about     - Show info about me")
    type_text("projects  - View my projects")
    type_text("contact   - Contact info")
    type_text("clear     - Clear the screen")
    type_text("help      - Show this menu")
    type_text("exit      - Exit program\n")

# Main loop
def main():
    boot()
    type_text("Welcome to your Developer Terminal.", 0.04)
    type_text("Type 'help' to see commands.\n")

    while True:
        cmd = input(">>> ").lower()

        if cmd == "about":
            show_about()
        elif cmd == "projects":
            show_projects()
        elif cmd == "contact":
            show_contact()
        elif cmd == "help":
            help_menu()
        elif cmd == "clear":
            clear()
        elif cmd == "exit":
            type_text("Shutting down...")
            break
        else:
            type_text("Command not found. Type 'help'.")

if __name__ == "__main__":
    main()

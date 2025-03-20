from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.align import Align
from time import sleep
import shutil
import os
import pyfiglet
import itertools

console = Console()

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def get_terminal_width():
    """Returns the current terminal width dynamically."""
    return shutil.get_terminal_size().columns

def center_ascii(text, width):
    """Centers ASCII text based on terminal width."""
    lines = text.split("\n")
    centered_lines = [line.center(width) for line in lines]
    return "\n".join(centered_lines)

def animated_banner():
    """Displays the 'WinDy' banner with a bounce animation."""
    width = get_terminal_width()
    ascii_art = pyfiglet.figlet_format("WinDy", font="slant")
    centered_ascii = center_ascii(ascii_art, width)

    for i in range(3):  # Bounce effect
        console.clear()
        console.print(Panel(Text(centered_ascii, style=f"bold cyan"), title="[bold magenta]WinDy Account Manager[/bold magenta]", border_style="bright_blue", expand=True))
        sleep(0.1)
        console.clear()
        console.print(Panel(Text(center_ascii(ascii_art, width + 2), style="bold cyan"), title="[bold magenta]WinDy Account Manager[/bold magenta]", border_style="bright_blue", expand=True))
        sleep(0.1)

def loading_animation(duration=4):
    """Displays a centered loading animation for the given duration."""
    width = get_terminal_width()
    loading_text = Text(" Loading... ", style="bold yellow")

    frames = ["⠏", "⠛", "⠹", "⠼", "⠶", "⠧"]  # Braille-style spinner
    spinner = itertools.cycle(frames)  # Infinite loop through frames

    with Live(Align.center(loading_text), refresh_per_second=10) as live:
        for _ in range(duration * 10):  # Adjust animation speed
            loading_text.plain = f" {next(spinner)} Loading... {next(spinner)} "
            live.update(Align.center(loading_text))
            sleep(0.1)

def display_menu():
    """Displays a formatted and centered menu."""
    width = get_terminal_width()
    menu_title = " TELEGRAM SCRAPER MENU "
    title_bar = "=" * ((width - len(menu_title)) // 2) + menu_title + "=" * ((width - len(menu_title)) // 2)

    menu_text = Text("\n" + title_bar + "\n", style="bold yellow")

    options = [
        ("1. Run Manager", "green"),
        ("2. Run Scraper", "green"),
        ("3. Run Adder", "green"),
        ("4. Run Manual Add", "green"),
        ("0. Exit", "red"),
    ]

    border = "=" * width
    menu_text.append(border + "\n", style="blue")
    for text, color in options:
        menu_text.append(text.center(width) + "\n", style=color)
    menu_text.append(border + "\n", style="blue")

    # Warning Note
    note_text = "Note: This is a free tool. If someone is selling it, you are being scammed."
    menu_text.append("\n" + note_text.center(width) + "\n", style="bold red")

    console.print(menu_text)

def main():
    """Main program loop with animations."""
    clear_screen()
    
    # Animated banner
    animated_banner()
    
    # Show loading animation before menu
    loading_animation()

    while True:
        clear_screen()
        animated_banner()
        display_menu()
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            os.system("python manager.py")
        elif choice == "2":
            os.system("python scraper.py")
        elif choice == "3":
            script_name = input("Enter script name (e.g., example.py): ").strip()
            os.system(f"python {script_name}")
        elif choice == "4":
            script_name = input("Enter manual add script name (e.g., manual_add.py): ").strip()
            os.system(f"python {script_name}")
        elif choice == "0":
            console.print("\n[bold red]Exiting...[/bold red]")
            break
        else:
            console.print("[bold red]Invalid option. Try again.[/bold red]")
        sleep(1)

if __name__ == "__main__":
    main()

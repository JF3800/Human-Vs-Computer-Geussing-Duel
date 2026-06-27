import random
from rich import print

print("[bold purple]Welcome To My Number Geussing Game :)[/bold purple]")

random_n = random.randint(1, 100)

user_number = int((input("What Number do you choose (for the computer to geuss)?")))

human_geuss = 0
computer_geuss = 0

while True:
    user_geuss = int(input("Geuss the number:"))
    human_geuss += 1
    if user_geuss == random_n:
        print(f"[bold green] CORRECT :) | You took {human_geuss} tries[/bold green]")
        break
    elif user_geuss > random_n:
        print("[bold red]Too High[/bold red]")
    else:
        print("[bold red]Too Low[/bold red]")

print("Now its computers turn")

low = 1
high = 100

while True:
    computer_geuss += 1
    geuss = (low + high)// 2
    if geuss == user_number:
        print(f"[bold green]The Computer Geusses: {geuss}[/bold green]")
        print(f"[bold cyan] Computer got it! in {computer_geuss} tries [/bold cyan]")
        print(f"[bold purple]You got it in {human_geuss}[/bold purple]")
        break
    elif geuss > user_number:
        high = geuss -1
        print(f"[bold red] The Computer Geusses: {geuss}[/bold red]")
    else:
        low = geuss +1 
        print(f"[bold red]The Computer Geusses: {geuss}[/bold red]")
if computer_geuss > human_geuss:
    print("[bold green]YOU WON!!!![/bold green]")
elif computer_geuss == human_geuss:
    print("[bold yellow]ITS A TIEEEE!!![/bold yellow]")
else:
    print("[bold red] YOU LOST!!![/bold red]")

input("\nPress Enter to exit...")
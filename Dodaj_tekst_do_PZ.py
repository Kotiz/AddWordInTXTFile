import os
import re  # Wyra¾enia regularne
from colorama import Fore, Style, init  # Kolorowanie tekstu

# Inicjalizujemy colorama dla Windowsa
init(autoreset=True)

from termcolor import colored

def modify_file(file_path, prefix):
    try:
        # Odczytujemy zawarto˜† pliku z kodowaniem CP852
        with open(file_path, 'r', encoding='cp852') as f:
            lines = f.readlines()

        # Modyfikujemy linie w pliku
        modified_lines = []
        for line in lines:
            parts = line.strip().split(';')
            if len(parts) >= 4:
                parts[3] = f"{prefix} {parts[3]}"  # Dodajemy tekst po trzecim ˜redniku
            modified_lines.append(';'.join(parts))

        # Zapisujemy zmodyfikowany plik z kodowaniem CP852
        with open(file_path, 'w', encoding='cp852') as f:
            f.write('\n'.join(modified_lines))

        # Komunikat o sukcesie w kolorze niebieskim
        print(colored(f"Plik {file_path} zostaˆ zmodyfikowany.", "blue"))
    except Exception as e:
        # Komunikat bˆ©du w kolorze czerwonym
        print(colored(f"Wyst¥piˆ bˆ¥d podczas modyfikacji pliku {file_path}: {e}", "red"))

def main():
    # —cie¾ka do folderu
    folder_path = r"C:\PZ"  # <-- Zmieä na wˆa˜ciw¥ ˜cie¾k©

    # Sprawdzamy, czy folder istnieje
    if not os.path.exists(folder_path):
        print(f"Bˆ¥d: Folder {folder_path} nie istnieje.")
        return

    # Pobieramy tekst od u¾ytkownika
    prefix = input("Podaj tekst, kt¢ry ma by† dodany: ")

    # Potwierdzenie poprawno˜ci wprowadzonego tekstu
    confirm = input(f"\nCzy wprowadzony tekst jest poprawny (t/n): {colored(prefix, 'green')}\n").strip().lower()
    if confirm != 't':
        print(Fore.RED + "Przerwano dziaˆanie programu.")
        return

    # Wyra¾enie regularne: Pliki z "_F" w nazwie i koäcz¥ce si© na "_"
    pattern = re.compile(r".*_F.*_\.(txt)$")

    found_files = False  # Flaga, czy znaleziono pasuj¥ce pliki

    # Przetwarzamy tylko pliki z rozszerzeniem .txt w katalogu
    for filename in filter(lambda f: f.endswith('.txt'), os.listdir(folder_path)):
        print(f"Sprawdzanie pliku: {filename}")  # Debug: Podgl¥d nazw plik¢w

        if pattern.match(filename):  # Dopasowanie do wzorca
            found_files = True
            file_path = os.path.join(folder_path, filename)
            modify_file(file_path, prefix)

    if not found_files:
        print("Nie znaleziono plik¢w speˆniaj¥cych kryteria.")

    # Zatrzymujemy program na koäcu
    input("\nNaci˜nij dowolny klawisz, aby zamkn¥† program.")

if __name__ == "__main__":
    main()

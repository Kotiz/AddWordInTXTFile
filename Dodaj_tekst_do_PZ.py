import os
import re
from colorama import Fore, Style, init  # Kolorowanie tekstu
import pyfiglet  # Powiększona czcionka

# Inicjalizujemy coloramę, aby działała poprawnie na Windowsie
init(autoreset=True)

def modify_file(file_path, prefix):
    try:
        # Odczytujemy zawartość pliku
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Modyfikujemy każdą linię
        modified_lines = []
        for line in lines:
            parts = line.strip().split(';')
            if len(parts) >= 4:
                parts[3] = f"{prefix} {parts[3]}"  # Dodajemy tekst po trzecim średniku
            modified_lines.append(';'.join(parts))

        # Zapisujemy zmodyfikowane linie do pliku
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(modified_lines))

        # Komunikat na niebiesko
        print(Fore.BLUE + f"Plik {file_path} został zmodyfikowany.")
    except Exception as e:
        # Komunikat błędu na czerwono
        print(Fore.RED + f"Wystąpił błąd podczas modyfikacji pliku {file_path}: {e}")

def main():
    # Ustalona ścieżka do folderu z plikami txt
    folder_path = r"C:\PZ"  # <-- Zmień na właściwą ścieżkę

    # Sprawdzamy, czy folder istnieje
    if not os.path.exists(folder_path):
        print(Fore.RED + f"Błąd: Folder {folder_path} nie istnieje.")
        return

    # Pobieramy tekst od użytkownika
    prefix = input("Podaj tekst, który ma być dodany: ")

    # Wyświetlenie wprowadzonego tekstu w powiększonej czcionce
    large_text = pyfiglet.figlet_format(prefix)
    print(large_text)
    confirm = input("Czy wprowadzony tekst jest poprawny? (t/n): ").strip().lower()

    if confirm != 't':
        print(Fore.RED + "Przerwano działanie programu.")
        return

    # Wyrażenie regularne: Pliki z "_F" w nazwie i kończące się na "_"
    pattern = re.compile(r".*_F.*_\.(txt)$")

    found_files = False  # Flaga, czy znaleziono pasujące pliki

    # Przetwarzamy pliki w katalogu
    for filename in os.listdir(folder_path):
        print(f"Sprawdzanie pliku: {filename}")  # Debug: Podgląd nazw plików

        if pattern.match(filename):  # Dopasowanie do wzorca
            found_files = True  # Zaznaczamy, że znaleziono pasujący plik
            file_path = os.path.join(folder_path, filename)
            modify_file(file_path, prefix)

    if not found_files:
        print(Fore.YELLOW + "Nie znaleziono plików spełniających kryteria.")

    # Komunikat na końcu, aby zatrzymać program
    input("\n" + Fore.GREEN + "Naciśnij dowolny klawisz, aby zamknąć program.")

if __name__ == "__main__":
    main()
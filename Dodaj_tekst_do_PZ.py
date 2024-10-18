import os
from termcolor import colored

def modify_file(file_path, prefix):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        modified_lines = []
        for line in lines:
            parts = line.strip().split(';')
            if len(parts) >= 4:
                parts[3] = f"{prefix} {parts[3]}"
            modified_lines.append(';'.join(parts))

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(modified_lines))

        print(colored(f"Plik {file_path} został zmodyfikowany.", "blue"))
    except Exception as e:
        print(colored(f"Wystąpił błąd podczas modyfikacji pliku {file_path}: {e}", "red"))

def main():
    folder_path = r"C:\PZ"  # <-- Zmień na właściwą ścieżkę
    prefix = input("Podaj tekst, który ma być dodany: ")

    # Potwierdzenie poprawności wprowadzonego tekstu
    print(f"\nCzy wprowadzony tekst jest poprawny: {colored(prefix, 'green')}\n")

    # Sprawdzenie plików w folderze
    files_found = False
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') and "_F" in filename and filename.endswith('_'):
            file_path = os.path.join(folder_path, filename)
            print(f"Sprawdzanie pliku: {filename}")
            modify_file(file_path, prefix)
            files_found = True

    if not files_found:
        print("Nie znaleziono plików spełniających kryteria.")

    input("\nNaciśnij dowolny klawisz, aby zamknąć program.")

if __name__ == "__main__":
    main()

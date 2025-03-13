i = input("Enter input file name, without the extension: ")
r = input("Enter result file name, without the extension: ")

def fasta_editor(i, r):
    with open(i, "r") as input, open(r, "w") as result:
        for x in input:
            if x.startswith(">"):
                head = x[1:].strip()
                split = head.split()
                access_number = split[0]
                name = f"{split[1]}_{split[2]}"
                n_head = f">{name}_{access_number.split('.')[0]}\n"
                result.write(n_head)
            else:
                result.write(x)

        print(f"Result file saved as: {r}")
        
def main():
    i = input("Podaj ścieżkę do pliku wejściowego FASTA: ")
    r = input("Podaj nazwę pliku wyjściowego (lub pełną ścieżkę): ")

    try:
        edytuj_naglowki(i, r)
    except FileNotFoundError:
        print("Nie znaleziono pliku o podanej ścieżce. Upewnij się, że ścieżka jest poprawna.")


if __name__ == "__main__":
    main()

i = input("Enter input file name, with extension: ")
r = input("Enter result file name, with extension: ")

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
        

fasta_editor(i, r)
input("")

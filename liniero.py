#This script has been modified, yet is credited to the following source
#"https://stackoverflow.com/questions/50856538/how-to-convert-multiline-fasta-files-to-singleline-fasta-files-without-biopython"

unlinear_fasta_file=input("Hello, input fasta file you want to linearize:")
file_name=input("Which will be te name of your output file?: ")
with open(unlinear_fasta_file) as fasta, open(file_name + ".txt", "w") as fasta_output:
    block = []

    for line in fasta:
        #code that makes headers
        if line.startswith('>'):
            if block:
                fasta_output.write(''.join(block) + '\n')
                block = []
            fasta_output.write(line)
        #code that stacks fastas
        else:
            block.append(line.strip())
#code that generates linearized files
    if block:
        fasta_output.write(''.join(block) + '\n')

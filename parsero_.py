#Fasta heading parsero
# the following program will help to generate a data frame from a linearized fasta file
#from linerio.py program
# by Isabela Avila R

#library import
import re
import pandas as pd
import csv 

#open desired txt file 
fasta_file=input("Hello, input linearized fasta file you want to modify:")
print("preparing file as dataframe")
#pattern library declaration
accesion_pattern=re.compile(r"(>[A-Z,\w,\.1]*)")
specie_pattern=re.compile(r"\[([A-Z,a-z,\s,a-z]*)\]")
fasta_pattern=re.compile(r"\b([M,A-Z]*)\b")


#list declaration for dataframe
df_accesion_list=[]
df_species_list=[]
df_fasta_list=[]
#code to make a list of accesions
with open(fasta_file, "r") as fasta_read:
    for line in fasta_read:
        line=line.rstrip()
        if line.startswith(">"):
            df_accesion=re.findall(accesion_pattern,line)
            df_accesion_list.append(df_accesion)

#Code to make a list of species
with open(fasta_file, "r") as fasta_read:
    for line in fasta_read:
        line=line.rstrip()
        if "[" in line:
            df_species=re.findall(specie_pattern,line)
            df_species_list.append(df_species)
#Code to make accesion list
with open(fasta_file, "r") as fasta_read:
    for line in fasta_read:
        line=line.rstrip()
        if line==line.upper():
            line=line.strip("\n")
            df_fasta=re.findall(fasta_pattern,line)
            df_fasta_list.append(df_fasta)


#For code modification use these testing statements
#print(df_accesion_list)
#print(df_species_list)
#print(df_fasta_clean)

#dataframe generation
fasta_df=pd.DataFrame()

#addition of columns to dataframe
fasta_df["Accesion"]=df_accesion_list
fasta_df["Species"]=df_species_list
fasta_df["Fasta sequence"]=df_fasta_list

print(fasta_df)

data_frame_name=input("Great! we have our fasta dataframe!  \n what name would you like for your exit file?: ")
fasta_df.to_csv(data_frame_name+".csv")

print("thank you for using parsero!")
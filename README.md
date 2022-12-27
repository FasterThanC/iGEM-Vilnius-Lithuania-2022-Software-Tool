# iGEM Vilnius-Lithuania 2022 Software Tool



[**Wiki page**](https://2022.igem.wiki/vilnius-lithuania/) of NanoFind team. 


## Description - GenFusMSA
**Disclaimer:** We want to be very clear that we did not create this software, we improved on it. The credit for designing this software tool goes to [**Vilnius-Lithuania-iGEM 2021**](https://2021.igem.org/Team:Vilnius-Lithuania), mainly to [**Ieva Pudžiuvelytė**](https://www.linkedin.com/in/ieva-pud%C5%BEiuvelyt%C4%97/). What we did was rewrite the programming code of this software to another language as well as add additional functionality. 

GenFusMSA is a script that generates multiple sequence alignment (MSA) file that can be used for fusion protein joined via linkers of choice modeling. This program supports [**small tool for bioinformatics manifesto**](https://github.com/pjotrp/bioinformatics).

It is a program that scans input full query-template .a3m files and pairs sequences according to their taxonomy ID. The paired sequences are joined via a peptide linker that is determined by the user, and the collection of sequences can be saved as an output .a3m file.

## Requirements
Download and install [**Python**](https://www.python.org/).

## Usage
1) Download GenFusMSA.py script and two .a3m input files.
2) Open the Terminal (command prompt/line) and enter the path towards the destination of the script. 

Inputs for the program are:
1. `input1` first .a3m input file [file]
2. `input2` second .a3m input file [file]
3. `linker` peptide linker [text]
4. `linkerRepeats` how many repeats of linker should be added [number]
5. `isProlonged` whether linker should be extended or not [boolean]

The .a3m file can be generated using external software. The program was tested with MSA files that were generated using [**HHblits**](https://toolkit.tuebingen.mpg.de/tools/hhblits) program.

The construction of the command that should be entered into the Terminal in order to run the script:

`python GenFusMSA.py input1 input2 linker linkerRepeats isProlonged`

Example of usage:
`python GenFusMSA.py 4CL_fullQT.a3m CHS_fullQT.a3m EAAAK 1 true`

This command generates MSA file for 4CL and CHS linked via prolonged EAAAK linker. The option to choose if the linker repeats is set by linkerRepeats (choose 0 or 1) and the option to choose prolonged linker by glycines (by 10 on both sides of the linker) is set by the last option (0 or 1).

The output of the program can be found in outputMSA.txt, outputMSA.csv and outputMSA.a3m file.

Get usage guide: `python GenFusMSA.py help`


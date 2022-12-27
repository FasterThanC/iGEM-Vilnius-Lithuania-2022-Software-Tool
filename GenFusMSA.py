import sys
import re

taxIds = [{}, {}]
matchedDict = {}

def main():
    args = sys.argv
    args.pop(0)
    
    if len(args) == 5:
        getFileData(args[0], 1)
        getFileData(args[1], 2)
        getMSA(args[2], int(args[3]), args[4] == "true")
    elif len(args) == 1 and args[0] == "help":
        usage()
    else:
        print("Run 'python GenFusMSA.py help' to get usage guide.")    
    
    return 0


def usage():
    print("""    Script extracts sequences that share the same TaxID from 2 MSA files.
          
    Usage:
    'python GenFusMSA.py input1 input2 linker linkerRepeats isProlonged'

    Arguments:
    input1          -> first .a3m input file [file];
    input2          -> second .a3m input file [file];
    linker          -> peptide linker [text];
    linkerRepeats   -> how many repeats of linker should be added [number];
    isProlonged     -> whether linker should be extended or not (true or false) [boolean];

    Example:
    'python GenFusMSA.py 4CL_fullQT.a3m CHS_fullQT.a3m EAAAK 1 true'

    Please, check outputMSA.txt, outputMSA.csv or outputMSA.a3m file for the output of the program.
    """)

def getFileData(inputFile, fileNumber):
    global taxIds
    input = open(inputFile, "r")
    taxIdsCount = 0
    fileNumber -= 1 # Get list index
    
    while True:
        headerLine = input.readline().strip()
        sequenceLine = input.readline().strip()
        
        if not headerLine or not sequenceLine:
            break
        else:
            taxIdsCount += 1
            
            if taxIdsCount == 1:
                taxId = "query"
                taxIds[fileNumber][taxId] = sequenceLine
            else:
                taxIdsList = re.findall("TaxID=(\d+)", headerLine)

                if len(taxIdsList) == 1:
                    taxId = taxIdsList[0]
                    taxIds[fileNumber][taxId] = sequenceLine
                else:
                    print("No tax id found in header line")
                    
            if fileNumber == 1 and taxId in taxIds[0].keys():
                matchedDict[taxId] = ""

    input.close()

def getMSA(linker, n, prolonged):
    global matchedDict, taxIds
    output1 = open("outputMSA.a3m", "w")
    output2 = open("outputMSA.txt", "w")
    output3 = open("outputMSA.csv", "w")
    print("Please, check the outputMSA.txt, outputMSA.csv or outputMSA.a3m file for the output of the program.")

    for id in list(reversed(sorted(matchedDict.keys()))):
        fusion = taxIds[0][id]
        
        if prolonged:
            fusion += "G" * 10
            fusion += linker * n
            fusion += "G" * 10
        else:
            fusion += linker * n
            
        fusion += taxIds[1][id]
        matchedDict[id] = fusion
        
        output1.write("id = " + id + "\n")
        output1.write(matchedDict[id] + "\n")
        output2.write("id = " + id + "\n")
        output2.write(matchedDict[id] + "\n")
        output3.write(f"{id},{matchedDict[id]}\n")
        
    output1.close()
    output2.close()
    output3.close()
    
main()

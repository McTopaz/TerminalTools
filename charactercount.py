import sys
import fileinput

def FromStandardInput():
    fi = fileinput.input()
    line = str(fi[0])
    parts = line.split()
    Print(parts)
    
def FromArguments():
    args = sys.argv[1:]
    Print(args)

def Print(array):
    if len(array) == 1:
        print(len(array[0]))
        return
    
    for item in array:
        print("%s: %s"%(item, len(item)))
    
    line = "".join(array)
    print("Total: %s"%(len(line)))

# =============================================================================
# === Main ====================================================================
# =============================================================================

if len(sys.argv) == 1:
    FromStandardInput()
if len(sys.argv) > 1:
    FromArguments()

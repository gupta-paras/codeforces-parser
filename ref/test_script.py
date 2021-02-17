import os
import shutil
import re
from termcolor import colored
from colorama import init
import sys
import subprocess
init()

q = str(sys.argv[1])
pretest_folder = 'pretests'

data_folder = os.path.join(pretest_folder, q)
local_input = 'input.txt'
local_output = 'output.txt'

pretests = list({e.replace("input_","").replace("output_", "").replace(".txt", "") for e in os.listdir(data_folder)})
pretests.sort()

for e in pretests:

    # execute script    
    input_src = os.path.join(data_folder, "input_{}.txt".format(e))
    output_src = os.path.join(data_folder, "output_{}.txt".format(e))
    
    shutil.copy(input_src, local_input)

    proc = subprocess.Popen(["run.bat", q], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    ret = proc.wait()
    if (ret): 
        print("program exited with return code: ",ret)
        print("traceback: " , err.decode('utf-8'))
    # compare output with folder output
    
    with open(input_src) as f:
        ref_in = f.read()
        
    with open(output_src) as f:
        ref_out = f.read()
    
    with open(local_output) as f:
        out = f.read()  

    ref_parsed = [e for e in re.split(r'\s+', ref_out) if e ]
    out_parsed = [e for e in re.split(r'\s+', out) if e ]
    
    print("-"*30)
    outcolor = 'green'
    if (ref_parsed != out_parsed):
        print(colored("pretest - {}: FAILED".format(e), 'red', attrs=['bold']))
        outcolor = 'red'
    else :
        print(colored("pretest - {}: PASSED".format(e), 'green', attrs=['bold']))

    if (ret): print(colored("RUNTIME ERROR", 'red', attrs=['bold']))
    print(colored(ref_in, 'yellow', attrs=['bold']))
    print(colored(ref_out, 'white', attrs=['bold']))
    print(colored(out if len(out_parsed) else "NO OUTPUT TO DISPLAY!!!", outcolor, attrs=['bold']))

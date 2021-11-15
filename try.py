import sys
from unittest.case import TestCase
def createTestCases():
    if filePath == '':
        return []
    fd = open(filePath, "r")
    inputStr = ""
    outputStr = ""
    allLines = fd.readlines()
    allTestCases = []
    i = 0
    while(i < len(allLines)):
        if allLines[i] == "Input:\n":
            inputStr = ""
            i += 1
            while(i < len(allLines) and allLines[i] != "Output:\n"):
                inputStr += allLines[i]
                i += 1
            if i >= len(allLines) or allLines[i] != "Output:\n":
                return [], False
            
        elif allLines[i] == "Output:\n":
            outputStr = ""
            i += 1
            while(i < len(allLines) and allLines[i] != "Input:\n"):
                outputStr += allLines[i]
                i += 1
            testCase = [inputStr, outputStr]
            allTestCases.append(testCase)
        else:
            i += 1
    return allTestCases, True


filePath = './testcases.txt'
print(createTestCases())

cmd = f"python3 {file_path} {"

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, stdin = subprocess.PIPE,shell=True)
    inputStr = b''
    inputStr = inputStr.encode()
    output, error =  process.communicate(input=inputStr)
    
    # Delete previous output
    output_window.delete(1.0, END)

    # Insert new output
    output_window.insert(1.0, output)

    # Insert Error to output box
    output_window.insert(1.0, error)
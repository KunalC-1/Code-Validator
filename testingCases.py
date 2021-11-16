from tkinter.filedialog import test
import unittest
import subprocess

def createTestCases():
    if testcases_file_path == '':
        return []
    try:
        fd = open(testcases_file_path, "r")
    except:
        return [], False
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
            outputStr = trimOutput(outputStr)
            testCase = [inputStr, outputStr]
            allTestCases.append(testCase)
        else:
            i += 1
    return allTestCases, True

def trimOutput(output):
    i = len(output) - 1
    while i >= 0:
        if output[i] == "\n":
            output = output[:i]
            i -= 1
        else:
            break
    return output

class TestCaseRunner(unittest.TestCase):
    
    def testRunner(self):
        for i in range(len(testCases)):
            with self.subTest(i=i):
                isTestCaseMatched = False
                cmd = f"python3 {program_path}"
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, stdin = subprocess.PIPE,shell=True)
                inputStr = testCases[i][0]
                inputStr = inputStr.encode()
                output, error =  process.communicate(input=inputStr)  
                output = trimOutput(output.decode())
                if len(error):
                    print(error.decode())
                    return
                else:
                    if output == testCases[i][1]:
                        isTestCaseMatched = True
                print (f"\nTest Case {i}   :    ✅") if (isTestCaseMatched) else print(f"\nTest Case {i}   :    ❌")
                try:
                    self.assertEqual(testCases[i][1], output)
                except AssertionError as e:
                    print("\nYour Output :")
                    print(output)
                    e.args = ""
                    raise

if __name__ == "__main__":
    global testCases, program_path
    testcases_file_path = input()
    program_path = input()
    testCases, valid = createTestCases()
    if valid:
        unittest.main()

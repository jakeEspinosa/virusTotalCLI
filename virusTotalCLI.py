# Script Module Importing

import hashlib
import json
import os
from virus_total_apis import PublicApi as VirusTotalPublicApi

# End of Script Module Importing

# Script Constants

API_KEY = ""

# End of Script Constants

# Script Functions

def DoesTheFileExist():
    while True:
        print("Please enter the absolute path to the desired file:")
        userInputtedFileName = input()
        doesItExist = os.path.isfile(userInputtedFileName)
        if doesItExist == True:
            break
        if doesItExist == False:
            print(userInputtedFileName + " does not exist/is not a file...")
    return userInputtedFileName

# End of Script Functions

# Main

if __name__ == '__main__':
    
    try:

        # Prompt the User for a File Name
    
        print("Welcome to Jake Espinosa's Virus Total Client!\n")
    
        file = DoesTheFileExist()
    
        # Hash the User-Inputted File
    
        md5Hash = hashlib.md5()
    
        with open(file, "rb") as fileToHash:
            fileToHashContent = fileToHash.read()
            md5Hash.update(fileToHashContent)
            fileDigest = md5Hash.hexdigest()
        
        # Pass File Hash to VirusTotal and Get JSON Data
    
        vt = VirusTotalPublicApi(API_KEY)
        response =  vt.get_file_report(fileDigest)
        responseJson = json.dumps(response, sort_keys=False, indent=4)

        # Process JSON Data
    
        responseJsonData = json.loads(responseJson)
        responseSet = responseJsonData['results']
        responseCode = responseSet['response_code']
        responseMsg = responseSet['verbose_msg']

        # Print Results

        print('\nResponse code: ' + str(responseCode) + '\n')
        print('Verbose message: ' + responseMsg)

    except KeyboardInterrupt:
        print('Ctrl+C entered, program terminating...')

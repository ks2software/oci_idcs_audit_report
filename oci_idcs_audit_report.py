from IdcsClient import AccessTokenManager
import json


# Author Richard Nuskind@KS2
# Created 8/8/2023 
CONFIG_FILE = 'tenancy.json'

def loadconfig(config_file):
    #load the file
    with open(config_file) as f:
        config_file = f.read().strip()
    # read the options from the file
    options = json.loads(config_file)
    return options 

def retrieveAccessToken(options):
    pass 

def main():
    #Call to load the configuration file
    options = loadconfig(CONFIG_FILE)

    print(options)
    # Use the AccessTokenManager to get a new token 



if __name__ == "__main__":
    main()

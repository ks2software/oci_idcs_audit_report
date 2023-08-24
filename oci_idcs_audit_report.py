from IdcsClient import AccessTokenManager
import json


# Author Richard Nuskind@KS2
# Created 8/8/2023 
CONFIG_FILE = 'tenancy.json'

# Load the tenancy information from the CONFIG_FILE
def load_config(config_file):
    with open(config_file) as f:
        config_file = f.read().strip()
    options = json.loads(config_file)
    return options 

# Function to retrieve a new token 
def retrieve_access_token(options):
    access_token_manager = AccessTokenManager(options)
    token = access_token_manager.getAccessToken()
    return token

def main():
    options = load_config(CONFIG_FILE)
    print(options)
    token = retrieve_access_token(options)
    print(token)



if __name__ == "__main__":
    main()

import os
import pickle
from IPython.display import display, Javascript, HTML
import time

# --- Global variable to store the API token ---
# This variable will be set by the function, potentially asynchronously from JS.

TOKEN_FILE_PATH = "nqch_API_token.pickle"

# --- Function to handle saving the token (called from JavaScript) ---
# This is a helper function that JavaScript will call back into the Python kernel.


        
def load_api_token():

    try:
        with open(TOKEN_FILE_PATH, "rb") as f:
            token_api = pickle.load(f)
        print(f"API token loaded from '{TOKEN_FILE_PATH}'.")
        return token_api
    except (EOFError, pickle.UnpicklingError, FileNotFoundError) as e:
        print(f"Corrupted or empty token file '{TOKEN_FILE_PATH}': {e}. Will prompt for new token.")
        _prompt_for_token_js()
    except Exception as e:
        print(f"An unexpected error occurred while loading token: {e}. Will prompt for new token.")
        _prompt_for_token_js()
    


    
# --- How to use it in your Jupyter notebook ---
# Call the function
#from utils_tokens
#get_or_prompt_for_api_token()
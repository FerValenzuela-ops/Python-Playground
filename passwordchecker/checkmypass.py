import requests
import hashlib
import sys



def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    reqs = requests.get(url)
    if reqs.status_code != 200:
        raise RuntimeError(
            f'Error fectching: {reqs.status_code}, check the api and try again')
    return reqs


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0    


def pwned_api_check(password): # we give hello
    # check password if exists in API response

    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # we transform hello to sha1password
    first5_char, tail = sha1password[:5], sha1password[5:] # once is transformed, we create two variables
    response = request_api_data(first5_char) # we call request_api_data with the firts 5 chars of the password transformed
    return get_password_leak_count(response, tail) # we return the first 5 chars and the rest as a tupple


def main(args):
    for doc in args:
        pwdfile = open(f'{doc}', 'r')  # file = sys.argv
        for line in pwdfile:
            for password in line.splitlines():
                count = pwned_api_check(password)
                if count:
                    print(f'"{password}" was found "{count}" times, you should probably change your password')
                else:
                    print(f'"{password}" was not found. Carry on!!')
                

  
    return '\nIn the file are no more words!'      
    
    
    
if __name__ == '__main__':    
    sys.exit(main(sys.argv[1:])) # file = sys.argv





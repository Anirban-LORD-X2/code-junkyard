import requests
import sys
import hashlib
def req_api_data(query_char):
    url= 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'Error fetching {res.status_code}, check tha api and try again')
    return res

def get_pass_leaks_count(hashes, hash_to_check):
    hashes= (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
        else:
            return 0
        
    
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail= sha1password[:5], sha1password[5:]
    response= req_api_data(first5_char)
    print(first5_char, tail)
    print(response)
    return get_pass_leaks_count(response, tail)

def main(args):
    for password in args:
        count=pwned_api_check(password)
    if count:
        print(f' {password} was found to have been breached {count} number of times, it is recommended to change the password')
    else:
        print(f'{password} was not found...Congratulations you are safe')
        
        
main(sys.argv[1:])
        


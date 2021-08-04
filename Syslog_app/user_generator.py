def user(username, password, email, image_file):
    return {'username': f'{username}', 
    'password': f'{password}', 'email': f'{email}', 
    'image_file': f'{image_file}'}
    

def user_login(email, login_state, remember, datetime):
    return {'email': f'{email}', 
    'login_state': f'{login_state}', 'remember': f'{remember}', 
    'datetime': f'{datetime}'}

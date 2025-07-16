from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    l = []
    for i in data['messages']:
        for j in users_id:
            if i['id'] == j:
                l.append(i.get("actor") or i.get("from"))
    ipt = input("User nomini kiriting: ")
    return l.count(ipt)


a = read_data("data/result.json")
print(find_user_message_count(a, find_all_users_id(a)))
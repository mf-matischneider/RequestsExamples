import requests
import pandas as pd


def test_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f'API call to {url} was successful')
        return 'Success'
    else:
        return 'Failure'
def get_all_users():
    payload = {}
    headers = {
        'x-org-id': '5abfa86b69381b778cd7e2be',
        'Accept': 'application/json',
        'x-api-key': '8819ada3791d0ee0e1d71587ff321253a5401a3a'

    }
    url = f"https://console.jumpcloud.com/api/v2/users?fields=&filter=&limit=100&skip=0&sort="
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()
def get_user_groups():
    payload = {}
    headers = {
        'x-org-id': '5abfa86b69381b778cd7e2be',
        'Accept': 'application/json',
        'x-api-key': '8819ada3791d0ee0e1d71587ff321253a5401a3a'

    }
    url = f"https://console.jumpcloud.com/api/v2/usergroups?fields=&filter=&limit=300&skip=0&sort="
    user_groups = []
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()
def get_user_groups_list():
    user_groups = get_user_groups()
    user_groups_df = pd.DataFrame(user_groups)
    return user_groups_df[['id', 'name']].itertuples()
def get_user_group_members_list(user_group_id):
    payload = {}
    headers = {
        'x-org-id': '5abfa86b69381b778cd7e2be',
        'Accept': 'application/json',
        'x-api-key': '8819ada3791d0ee0e1d71587ff321253a5401a3a'

    }
    url = f"https://console.jumpcloud.com/api/v2/usergroups/{user_group_id}/members?limit=100&sort="
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    user_groups = get_user_groups_list()
    user_group_ids = []
    user_group_names = []
    for user_group in user_groups:
        user_group_ids.append(user_group.id)
        user_group_names.append(user_group.name)








import requests
BASE_URL = "https://chrisbrooks.pythonanywhere.com/api/programmers"

def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    response = requests.get(BASE_URL)
    data = response.json()
    return len(data.get("programmers", []))


def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    response = requests.get(f"{BASE_URL}/{pid}")
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
    response = requests.get(f"{BASE_URL}/by_first_name/{first_name}")
    data = response.json().get("programmers", [])
    if data:
        programmer = data [0]
        return f"{programmer['first']}{programmer['last']}"
    else:
        return None

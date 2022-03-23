from biorhythm.dao import friendDAO, userDAO


def find_users_by_username(username: str):
    results = userDAO.findUsersByUsername(username)
    return results


def find_request(requesterID: str, requesteeID: str):
    friendDAO.find_friend_request(requesterID, requesteeID)


def send_friend_invite(userID: str, friendID: str):
    friendDAO.create_friend_request(userID, friendID)

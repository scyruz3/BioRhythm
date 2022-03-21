from biorhythm.dao import friendDAO


def send_friend_invite(userID: str, friendID: str):
    friendDAO.create_friend_request(userID, friendID)

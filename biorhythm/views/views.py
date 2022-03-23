from crypt import methods
from io import BytesIO
from biorhythm import app
from flask import session, send_file
from biorhythm.utils import getImageFromBinary
from biorhythm.dao import userDAO


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, "PNG", quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype="image/jpeg")


@app.route("/docs/pfp")
def serve_img():
    img = getImageFromBinary.getImageFromBinary(
        userDAO.getUserImgBin(session["userId"])
    )
    return serve_pil_image(img)


@app.route("/docs/pfp/<friendID>", methods=["GET"])
def serve_friend_img(friendID):
    print(friendID)
    img = getImageFromBinary.getImageFromBinary(userDAO.getUserImgBin(friendID))
    return serve_pil_image(img)

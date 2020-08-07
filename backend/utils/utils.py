import os
import base64
from backend.core.config import settings


def img_base64(img_name):
    with open(os.path.join(settings.BASEDIR, 'tmp/images', img_name), 'rb') as img:
        base64_img = base64.b64encode(img.read()).decode('ascii')
    image = "data:image/jpg;base64,{}".format(base64_img)
    return image

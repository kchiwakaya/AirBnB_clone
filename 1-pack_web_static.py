#!/usr/bin/python3
# generates a .tgz archive from the contents of web_static.
import os.path
from fabric.api import local
from datetime import datetime



def do_pack():
    """
    Create archive of the directory web static.
    """
    dateTime = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dateTime.year,
                                                         dateTime.month,
                                                         dateTime.day,
                                                         dateTime.hour,
                                                         dateTime.minute,
                                                         dateTime.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

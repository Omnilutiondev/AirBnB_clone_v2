#!/usr/bin/python3
""" This Fabric script generates a .tgz archive file from the
content of the web_static project files"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """ command generates a .tgz archive """
    local("mkdir -p versions")
    now = datetime.utcnow()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    result = local("tar -cvzf {} web_static".format(archive_name))

    if result.succeeded:
        return archive_name
    else:
        return None

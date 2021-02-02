"""
If you set STATIC_URL to a static value, then each time you update a CSS file, a JavaScript file, or an image,
you and your website visitors will need to clear the browser cache in order to see the changes.
There is a trick to work around clearing the browser's cache.
It is to have the timestamp of the latest changes shown in STATIC_URL.
Whenever the code is updated, the visitor's browser will force the loading of all new static files.

In this module, a timestamp is put in STATIC_URL for Git users.

"""
import subprocess
from datetime import datetime


def get_git_changeset_timestamp(absolute_path):
    repo_dir = absolute_path
    git_log = subprocess.Popen(
        "git log --pretty=format:%ct --quiet -1 HEAD",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        cwd=repo_dir,
        universal_newlines=True,
    )

    timestamp = git_log.communicate()[0]
    try:
        timestamp = datetime.utcfromtimestamp(int(timestamp))
    except ValueError:
        # Fallback to current timestamp
        return datetime.now().strftime('%Y%m%d%H%M%S')
    changeset_timestamp = timestamp.strftime('%Y%m%d%H%M%S')
    return changeset_timestamp

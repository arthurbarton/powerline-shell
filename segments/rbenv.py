import subprocess


def add_rbenv_segment(powerline):
    try:
        p1 = subprocess.Popen(["rbenv", "version-name"], stdout=subprocess.PIPE)
        version = p1.communicate()[0].decode("utf-8").rstrip()
        if len(version) <= 0:
            return

        if version == "system":
            return
        else:
            powerline.append(' %s ' % version, Color.VIRTUAL_ENV_FG, Color.VIRTUAL_ENV_BG)

    except OSError:
        return

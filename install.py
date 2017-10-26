#!/usr/bin/env python3

import subprocess
subprocess.run(["cp", "my-config.json", "~/.powerline-shell.json"], check=True)
subprocess.run(["python3", "setup.py", "build"], check=True)
subprocess.run(["python3", "setup.py", "install", "--root=$HOME/.local"], check=True)

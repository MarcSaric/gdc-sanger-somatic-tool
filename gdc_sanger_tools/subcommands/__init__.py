import importlib
import os
from types import SimpleNamespace

import stringcase as sc


def find_commands():
    _, _, files = list(os.walk(os.path.dirname(__file__)))[0]
    commands = {}
    for file in files:
        if file in ['base.py', '__init__.py']:
            continue
        if not file.endswith('.py'):
            continue
        command, _ = os.path.splitext(file)
        mod = importlib.import_module('.' + command, package=__name__)
        commands[command] = getattr(mod, sc.pascalcase(command))
    return commands

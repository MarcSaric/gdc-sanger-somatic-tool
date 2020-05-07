"""Tests the `gdc_sanger_tools.subcommands.base.Subcommand` class"""
import unittest
from types import SimpleNamespace

from gdc_sanger_tools.subcommands import base as MOD


class SubcommandTestCase(unittest.TestCase):
    CLASS_OBJ = MOD.Subcommand

    def setUp(self):
        self.options = SimpleNamespace()

    def test_main_raises_NotImplementedError(self):
        with self.assertRaises(NotImplementedError):
            self.CLASS_OBJ.main(options=self.options)

    def test_instance_raises_TypeError(self):
        with self.assertRaisesRegex(TypeError, 'abstract methods'):
            self.CLASS_OBJ()

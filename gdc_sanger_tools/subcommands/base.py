"""
Abstract base class for all subcommands in gdc-sanger-tools.
"""
from abc import ABCMeta, abstractmethod

import stringcase as sc

from gdc_sanger_tools.utils import ArgParserT, NamespaceT


class Subcommand(metaclass=ABCMeta):
    DESCRIPTION = None
    ARGUMENTS = None

    @classmethod
    @abstractmethod
    def __add_arguments__(cls, parser: ArgParserT):
        """Add the arguments to the parser"""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def main(cls, options: NamespaceT) -> None:
        """
        The default function when the subcommand is selected.  Returns None if
        executed successfully.
        """
        raise NotImplementedError

    @classmethod
    def __get_description__(cls):
        """
        Optionally returns description
        """
        return None

    @classmethod
    def setup_parser(cls, subparsers: ArgParserT) -> ArgParserT:
        """Adds the given subcommand to the subparsers."""
        subparser = subparsers.add_parser(
            name=sc.snakecase(cls.__name__), description=cls.__get_description__()
        )

        cls.__add_arguments__(subparser)
        # subparser.set_defaults(func=cls.main)
        return subparser

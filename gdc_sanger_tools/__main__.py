"""
Main entrypoint for all gdc-sanger-tools. 
"""
import argparse
import datetime
import sys
from signal import SIG_DFL, SIGPIPE, signal

from gdc_sanger_tools.logger import Logger
from gdc_sanger_tools.subcommands import find_commands

signal(SIGPIPE, SIG_DFL)


def setup_parser(subcommands):
    parser = argparse.ArgumentParser("GDC Sanger Tools")
    subparser = parser.add_subparsers(dest="subcommand")

    for command in subcommands:
        command.setup_parser(subparser)

    return parser


def main(argv=None, extra_subparser=None):
    """
    The main method for gdc-sanger-tools. 
    """
    # Setup logger
    Logger.setup_root_logger()

    logger = Logger.get_logger("main")

    # Get args
    p = argparse.ArgumentParser("GDC Sanger Tools")
    subparsers = p.add_subparsers(dest="subcommand")
    subparsers.required = True

    found_subcommands = find_commands()
    subcommands = list(found_subcommands.values())
    parser = setup_parser(subcommands)

    args = parser.parse_args(argv)

    # Run
    # options.func(options)

    logger.info(args)
    # Finish
    logger.info("Finished!")


if __name__ == '__main__':
    main()

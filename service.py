# -*- coding: utf-8 -*-

import argparse


def configure_parser(d_count):
    console_parser = argparse.ArgumentParser(
        prog=u'Disk info',
        description=u'Service for obtain information about disks'
    )

    console_parser.add_argument(
        u'-d',
        type=int,
        choices=range(0, d_count),
        help=u'Disk number'
    )
    return console_parser
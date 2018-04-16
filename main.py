# -*- coding: utf-8 -*-
from sys import platform, exit
from service import configure_parser

# Import worker by the our system
if platform == "linux" or platform == "linux2":
    from linux import disk
elif platform == "win32":
    from win import disk


if __name__ == u"__main__":
    # Take information about system about disks
    _sys_disks = disk.Information()
    # Create console parser
    parser = configure_parser(_sys_disks.count())
    # Takes arguments
    namespace = parser.parse_args()

    if namespace.d is None:
        # Print information about hardware disks
        devices = _sys_disks.devices()
        for device in devices:
            print(_sys_disks.device_to_str(device))
    else:
        # Print information about partitions by disk (namespace.d is int number)
        partitions = _sys_disks.partitions(namespace.d)
        for partition in partitions:
            print(_sys_disks.partition_to_str(partition))

    # Exit from program
    exit(0)

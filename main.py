# -*- coding: utf-8 -*-
from sys import platform, exit
from service import configure_parser

# Import worker by the system
if platform == "linux" or platform == "linux2":
    from linux import disk
elif platform == "win32":
    from win import disk


if __name__ == u"__main__":
    # Installed in the system drives
    _sys_disks = disk.Information()
    # Create console parser
    parser = configure_parser(_sys_disks.count())
    namespace = parser.parse_args()

    if namespace.d is None:
        devices = _sys_disks.devices()
        for device in devices:
            print(_sys_disks._device_to_str(device))
    else:
        partitions = _sys_disks.partitions(namespace.d)
        for partition in partitions:
            print(_sys_disks._partition_to_str(partition))

    # Exit from program
    exit(0)

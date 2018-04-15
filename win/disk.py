# coding=utf-8
# -*- coding: utf-8 -*-

from base import AbstractDisk
import wmi


class Information(AbstractDisk):
    @property
    def _devices(self):
        return [physical_disk for physical_disk in wmi.WMI().Win32_DiskDrive()]

    def count(self):
        return len(self._devices)

    def devices(self):
        _devices = list()
        for number, physical_disk in enumerate(self._devices):
            _devices.append(
                {
                    u'number': number,
                    u'name': physical_disk.Model,
                    u'size': float(physical_disk.Size)/(10**6)
                }
            )
        return _devices

    def partitions(self, number):
        _partitions = list()
        for partition in self._devices[number].associators("Win32_DiskDriveToDiskPartition"):
            _partitions.append(
                {
                    u'name': partition.Caption.encode("UTF"),
                    u'size': float(partition.Size)/(10**6)
                }
            )
        return _partitions

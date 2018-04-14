# coding=utf-8
# -*- coding: utf-8 -*-

import parted
from base import AbstractDisk


class Information(AbstractDisk):
    @property
    def _devices(self):
        return [device for device in parted.getAllDevices()]

    def count(self):
        return len(self._devices)

    def devices(self):
        _devices = list()
        for number, device in enumerate(self._devices):
            _devices.append(
                {
                    u'number': number,
                    u'name': device.model,
                    u'size': device.getSize(unit="MB")
                }
            )
        return _devices

    def partitions(self, number):
        _partitions = list()
        _disk = parted.Disk(self._devices[number])
        for partition in _disk.partitions:
            _partitions.append(
                {
                    u'name': partition.name if self.name_or_path(partition) else partition.path,
                    u'size': partition.getSize(unit="MB")
                }
            )
        return _partitions

    @staticmethod
    def name_or_path(partition):
        if partition.name is not None:
            if len(partition.name) == 0:
                return False
            else:
                return True

        return False

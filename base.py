# coding=utf-8
# -*- coding: utf-8 -*-


class AbstractDisk(object):
    @property
    def _devices(self):
        raise NotImplementedError("Subclasses should implement this!")

    @staticmethod
    def device_to_str(device):
        return '{} {} {:.1f}'.format(device['number'], device['name'], device['size'])

    @staticmethod
    def partition_to_str(_disk):
        return '{} {:.1f}'.format(_disk['name'], _disk['size'])

    def count(self):
        raise NotImplementedError("Subclasses should implement this!")

    def devices(self):
        raise NotImplementedError("Subclasses should implement this!")

    def partitions(self, number):
        raise NotImplementedError("Subclasses should implement this!")

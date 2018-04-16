# coding=utf-8
# -*- coding: utf-8 -*-


class AbstractDisk(object):
    '''
        Abstract class for all implementations
    '''
    @property
    def _devices(self):
        '''

        :return: list
            list of active hard disks
        '''
        raise NotImplementedError("Subclasses should implement this!")

    @staticmethod
    def device_to_str(device):
        '''

        :param device: dict
            device object (json)
        :return: str
            String representation of device

        '''
        return '{} {} {:.1f}'.format(device['number'], device['name'], device['size'])

    @staticmethod
    def partition_to_str(partition):
        '''

        :param partition: dict
            partition object (json)
        :return: str
            String representation of partition

        '''
        return '{} {:.1f}'.format(partition['name'], partition['size'])

    def count(self):
        '''

        :return: int
            Count of disk

        '''
        raise NotImplementedError("Subclasses should implement this!")

    def devices(self):
        '''

        :return: list
            List of dict like objects (Devices)

        '''
        raise NotImplementedError("Subclasses should implement this!")

    def partitions(self, number):
        '''

        :param number: int
            Number of disk
        :return: list
            List of dict like objects (partitions on disk)

        '''
        raise NotImplementedError("Subclasses should implement this!")

#!/bin/python3
# -*- coding: utf-8 -*-
import re as regex


def report_exit(label):
    print(label)
    exit()


def validate_input(value):

    if not len(value) or len(value) > 8:
        report_exit('Input size must be between 1 and 8 digits.')

    if not regex.match('\d[0-1]', value):
        report_exit('Input values must be number between 0 and 1.')


def convert_binary_to_decimal(binary, size=-1, decimal=-1):

    if decimal == -1:
        size = len(binary)
        decimal = 0

    exp = size - 1
    multiplier = 2**exp
    current_id = abs(size - len(binary))
    decimal += int(binary[current_id]) * exp

    if size > 1:
        return convert_binary_to_decimal(binary, size - 1, decimal)

    return decimal


if __name__ == "__main__":
    binary_input = input('Type here your binary digits: ')

    validate_input(binary_input)

    decimal = convert_binary_to_decimal(binary_input)

    report_exit(f'Your decimal value is {decimal}')

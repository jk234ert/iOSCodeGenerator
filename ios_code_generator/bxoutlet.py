# -*- coding: utf-8 -*-
__author__ = 'banxi'
from .bxuimodel_core import generate


def main():
    text = generate('outlet')
    print(text.decode('utf-8'))


if __name__ == '__main__':
    main()
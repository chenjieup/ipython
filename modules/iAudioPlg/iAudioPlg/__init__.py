#!/bin/env python
# -*- coding: utf8 -*-

import argparse
from iAudioPlg.version import __version__
from iAudioPlg.command import *
#from pythong.project import prompt_classifiers, prompt_new_project


def parse_command():
    p = argparse.ArgumentParser()
    #p.add_argument('name', nargs='?', default='',
    #               help='name of project to be created')
    p.add_argument('--version', action='version',
                   version="Pythong version {}".format(__version__))
    p.add_argument('-l', '--label', action='store_true',
                   help='add PyPI classifiers to your pythong')
    p.add_argument('-p', '--pin', nargs='+', type=str, action='append',
                   help='add files/directories to your pythong\'s manifest')
    p.add_argument('-s', '--snap', action='store_true',
                   help='create a project skeleton without any prompting')
    p.add_argument('-w', '--wash', action='store_true',
                   help='clean your pythong of messy build/dist/egg/pyc files')
    args = p.parse_args()
    if args.label:
	print("test1")
	wavread()
        #label(prompt_classifiers())
    elif args.pin:
        #pin(args.pin)
	print("test2")
    elif args.wash:
        #wash()
	print("test3")
    else:
        #prompt_new_project(args.name, args.snap)
	print("test4")
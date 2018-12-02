#!/usr/bin/env python

import argparse
import json
import os
import requests

def main():
    parser = argparse.ArgumentParser(description='Downloads issues from github and save as CSV')
    exclusive = parser.add_mutually_exclusive_group(required=True)
    exclusive.add_argument(
        '--files', nargs='+', type=argparse.FileType, metavar='FILE',
        help='Load previously saved JSON')
    exclusive.add_argument(
        '--github', metavar='USER/REPO',
        help='Load issues from USER/REPO')
    parser.add_argument(
        '--save_json', metavar='DIR',
        help='Save JSON to given directory')
        
    args = parser.parse_args()
    parser.print_help()
    
if __name__ == '__main__':
    main()
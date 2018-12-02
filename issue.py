#!/usr/bin/env python

import argparse
import csv
import itertools
import json
import os
import requests
import sys


def main():
    parser = argparse.ArgumentParser(description='Downloads issues from github and save as CSV')
    exclusive = parser.add_mutually_exclusive_group(required=True)
    exclusive.add_argument(
        '--files', nargs='+', type=argparse.FileType('r'), metavar='FILE',
        help='Load previously saved JSON')
    exclusive.add_argument(
        '--github', metavar='USER/REPO',
        help='Load issues from USER/REPO')
    parser.add_argument(
        '--save_json', dest='save_json', metavar='DIR',
        help='Save JSON to given directory')
        
    args = parser.parse_args()
    if args.github:
        jsons = get_github_jsons(args.github)
    elif args.files:
        jsons = get_file_jsons(args.files)
    else:
        raise Exception('Unexpected args: {}'.format(args))
    
    if args.save_json:
        save_json(jsons, args.save_json)
        
    issues = parse(jsons, field_selector)
    to_csv(issues)
    
def field_selector(record):
    return [
        record['number'], record['user']['login'],
        record['state'], record['created_at'], record['closed_at'],
        'PR' if hasattr(record, 'pull_request') else 'ISSUE',
        ' '.join([label['name'] for label in record['labels']]),
        record['title']
    ]
    
def get_github_jsons(repo):
    print('TODO: get_github_jsons')
    return ['[]']
    
def get_file_jsons(files):
    return [file.read() for file in files]
            
def save_json(jsons, dir):
    print('TODO: save_json')

def parse(jsons, field_selector):
    data_lists = [json.loads(json_string) for json_string in jsons]
    records = itertools.chain(*data_lists)
    return [field_selector(record) for record in records]
    
def to_csv(issues):
    writer = csv.writer(sys.stdout)
    for issue in issues:
        writer.writerow(issue)

    
if __name__ == '__main__':
    main()
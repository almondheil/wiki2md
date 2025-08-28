#!/usr/bin/env python3

"""
wiki2md

Convert .wiki notes to .md so you can share them easily.
"""

import argparse
import sys

#import misletoe # overkill?

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def wiki_to_markdown(lines):

    return lines

def main():
    # parse
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='path to input .wiki file')
    parser.add_argument('-o', '--output', help='path to output .md file')
    args = parser.parse_args()

    # print warnings if filenames don't match what we expect
    if not args.file.endswith('.wiki'):
        eprint(f'WARNING: Input file {args.file} does not end with .wiki')
    if args.output and not args.output.endswith('.md'):
        eprint(f'WARNING: Output file {args.output} does not end with .md')

    # read the input lines into memory all at once
    with open(args.file, 'r') as infile:
        wiki_lines = infile.readlines()

    # convert to markdown
    md_lines = wiki_to_markdown(wiki_lines)

    # either write to args.output (if provided) or print to stdout
    if args.output:
        with open(args.output, 'w') as outfile:
            outfile.writelines(md_lines)
    else:
        print(''.join(md_lines))

    return 0

if __name__ == '__main__':
    exit(main())

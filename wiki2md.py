#!/usr/bin/env python3

"""
wiki2md

Convert .wiki notes to .md so you can share them easily.
"""

import argparse
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def handle_inline_features(l):
    words = l.split(' ')
    output_words = words

    in_code = False
    for index, w in enumerate(words):
        # toggle whether we're in a code block
        if w.__contains__('`'):
            in_code = not in_code
            # no replacement here

        # skip if we're parsing code right now
        if in_code:
            pass

        if w.__contains__('*'):
            w = w.replace('*', '**')

        if w.__contains__('_'):
            w = w.replace('_', '*')

        # update output for word
        output_words[index] = w

    return ' '.join(output_words)

def handle_header(l):
    # split the line into parts. the title is *rest, except the ending ===
    start, *rest = l.split(' ')
    title = ' '.join(rest[:-1])

    # turn the start (multiple =s) into just as many #s and re-add it to the line
    start = start.replace('=', '#')
    header = start + ' ' + title + '\n'
    return header

def wiki_to_markdown(lines):
    output_lines = lines

    in_code_fence = False
    for index, l in enumerate(lines):
        # start or end a code fence
        if not in_code_fence and l.lstrip().startswith('{{{'):
            l = l.replace('{', '`')
            in_code_fence = True
            output_lines[index] = l
        elif in_code_fence and l.lstrip().startswith('}}}'):
            l = l.replace('}', '`')
            in_code_fence = False

        # don't evaluate other parts if we're parsing code right now
        if in_code_fence:
            pass

        # turn wiki headers into markdown headers
        if l.startswith('='):
            l = handle_header(l)

        # handle inline features of the line
        l = handle_inline_features(l)

        # update output for line
        output_lines[index] = l

    return output_lines

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

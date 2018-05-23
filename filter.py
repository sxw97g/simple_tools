import subprocess
import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument('file_in', type=str, help='Input file' )
parser.add_argument('file_out', type=str, help='output file' )
parser.add_argument('pattern_start', type=str, help='parttern start' )
parser.add_argument('pattern_end', type=str, help='parttern end' )

args = parser.parse_args()

f2 = open(args.file_out, 'w')
no_found_list = []
f1 = open(args.file_in, 'r')
lines_a = f1.readlines()

for line1 in lines_a:
        if line1 == '\n':
            break
        m = re.search(args.pattern_start + '(.+?)' +  args.pattern_end, line1)
        if m:
            found = m.group(1)
            f2.write(found + '\n')

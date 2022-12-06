import argparse
import subprocess
import sys
import tokens

SESSION = tokens.session
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2022)
parser.add_argument('--day', type=int, default=6)
args = parser.parse_args()

cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session={}"'.format(
        args.year, args.day, SESSION)
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
# print(output, end='')
# print('\n'.join(output.split('\n')[:10]), file=sys.stderr)


text_file = open(f"in\\{args.day}.txt", "w")
n = text_file.write(output)
text_file.close()
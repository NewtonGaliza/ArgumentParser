from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('name', help='say your name')

args = parser.parse_args()
print('Hello {}'.format(args.name))

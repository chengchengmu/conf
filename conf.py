#!/usr/bin/env python
# Configuration rendering engine
# See https://docs.python.org/2.4/lib/node109.html for template format

import click
from string import Template
import yaml
import re

# SUPPORTED_BACKENDS=['ssm', 'file']


# TODO unittest
# TODO add json or other input file format support
def render_template(template_file, subs):
  template = None
  with open(template_file) as f:
    template = Template(f.read())
  res = template.substitute(subs)
  return res

# TODO unittest
def get_conf_from_files(d, input_files):
  for input_file in input_files:
    with open(input_file) as inputf:
      d.update(yaml.load(inputf.read()))

# TODO unittest in case of files
def render(template_file, prefix, input_files):

  d = {}
  get_conf_from_files(d, input_files)
  res = render_template(template_file, d)
  print res

@click.command()
# @click.option('--priority', type=click.Choice(SUPPORTED_BACKENDS))
@click.argument('template_file', type=click.Path(exists=True))
@click.option('--prefix', '-p', multiple=True)
@click.option('--input_file', multiple=True)
# TODO add output file option
# @click.argument('--priority', nargs=2, type=click.Choice(SUPPORTED_BACKENDS))
def main(template_file, prefix, input_file):
  render(template_file, prefix, input_file)

if __name__ == '__main__':
  main()



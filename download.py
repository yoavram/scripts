# -*- coding: utf-8 -*-
"""
Download a file from a url to the local filesystem.

Created on Mon Mar  14 18:14:22 2016

@author: yoav@yoavram.com
"""
from urllib.request import urlretrieve
from urllib.parse import urlparse
import click

@click.command()
@click.argument('url')
@click.argument('filename', required=False)
def download(url, filename):
	if filename is None:
		filename = urlparse(url).path.split('/')[-1]
	urlretrieve(url, filename)


if __name__ == '__main__':
    download()

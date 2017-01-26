# -*- coding: utf-8 -*-
from source import *
import requests
import argparse
import urllib

parse = argparse.ArgumentParser()
parse.add_argument("id_number", type=int, help="id number")
parse.add_argument("-p", "--playlist", action="store_true",
                   help="id number is for playlist if specified \
                   or for single if not")
args = parse.parse_args()


def download_playlist(url):
    pass


def download_single(url):
    r = requests.get(url)
    song_name = r.json()['songs'][0]['name']
    mp3_url = r.json()['songs'][0]['mp3Url']
    print("Downloading......")
    urllib.request.urlretrieve(mp3_url, song_name + '.mp3')
    print("Complete!")

if args.playlist:
    playlist_url = playlist_format % args.id_number
    download_playlist(playlist_url)
else:
    single_url = single_format % (args.id_number, args.id_number)
    download_single(single_url)

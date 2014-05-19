from converter import Converter
c = Converter()

from sys import argv

info = c.probe(argv[1])

conv = c.convert(argv[1], argv[2], {
    'format': 'mp4',
    'audio': {
        'codec': 'mp3',
        'samplerate': 11025,
        'channels': 2
    },
    'video': {
        'codec': 'h264',
        'width': 720,
        'height': 400,
        'fps': 15
    }})

try:
    for timecode in conv:
        print "Converting (%f) ...\r" % timecode
except Exception as e:
    print e
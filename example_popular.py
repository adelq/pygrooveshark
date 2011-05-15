#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tempfile
import subprocess

import grooveshark

client = grooveshark.Client()
client.init()
null = open('/dev/null', 'wb')
for i, song in enumerate(client.popular()):
    print '%i: %s - %s - %s' % (i + 1, song.name, song.artist[0], song.album[0])
    stream, size = song.get_stream()
    output = tempfile.NamedTemporaryFile(suffix='.mp3', prefix='grooveshark_')
    output.write(stream.read(524288))
    process = subprocess.Popen(['/usr/bin/mplayer', output.name], stdout=null, stderr=null)
    data = stream.read(2048)
    while data:
        output.write(data)
        data = stream.read(2048)
    process.wait()
    output.close()
null.close()
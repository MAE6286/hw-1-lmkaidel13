#!/usr/bin/env bash

scriptdir="$( cd "$(dirname "$0")" ; pwd -P )"

hwdir=$scriptdir

python -m compileall $hwdir/mooc.py

destdir=$hwdir

cp $hwdir/__pycache__/mooc.cpython-36.pyc $destdir/mooc.pyc


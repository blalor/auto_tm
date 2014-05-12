#!/bin/bash

cd "$( dirname $0 )"

# Set the drive name that we mount for our backups 
vol_mount="$( ./get_destinations.py )"

if [ -n "${vol_mount}" ]; then
	# Drive is mounted, so: backup and then eject after
    tmutil startbackup -b
    diskutil eject "${vol_mount}"
fi

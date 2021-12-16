#!/bin/sh

NOW=$(date +"%Y-%m-%d")
pg_dump postgres -U postgres -h postgres -p 5432 | gzip > /path/to/backupname-$NOW.gzip
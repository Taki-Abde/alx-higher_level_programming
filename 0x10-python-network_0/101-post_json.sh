#!/bin/bash
# Post Request & made by ABDE
curl -sLX POST -H 'Content-Type: application/json' -d @"$2" "$1"

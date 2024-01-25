#!/bin/bash
# Print curl content size and made by ABDE
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2

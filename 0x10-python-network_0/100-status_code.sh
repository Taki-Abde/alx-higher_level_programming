#!/bin/bash
# Post Request & made by ABDE
curl -sLIw '%{http_code}' "$1" -o /dev/null

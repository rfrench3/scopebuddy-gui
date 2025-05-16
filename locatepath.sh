#!/bin/bash

# locatepath.sh - Find the full path of a given program

if [ -z "$1" ]; then
    echo "Usage: $0 <program-name>" >&2
    exit 1
fi

command -v "$1"

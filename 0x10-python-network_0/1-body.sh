#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the2
# body of the response
curl -s -L "${1}"

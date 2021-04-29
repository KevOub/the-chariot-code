#!/bin/bash

# echo $(( ($(date --date="031122" +%s) - $(date --date="021020" +%s) )/(60*60*24) ))
echo $(( ($(date --date="031122" +%s) - $(date --date="$1" +%s) )/(60*60*24) ))
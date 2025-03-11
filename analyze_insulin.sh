#!/bin/bash

sed '/ORIGIN/d; /\/\//d' preproinsulin-seq.txt. | tr -d '[:digit:] [:space:]' >  preproinsulin-seq-clean.txt
preproinsulin=$(cat preproinsulin-seq-clean.txt)
# echo "$preproinsulin"

grep -o '[a-z]' preproinsulin-seq-clean.txt | tr -d '\n' | cut -c1-24>  isinsulin-seq-clean.txt
isinsulin=$(cat isinsulin-seq-clean.txt)
# echo "$isinsulin"

grep -o '[a-z]' preproinsulin-seq-clean.txt | tr -d '\n' | cut -c25-54 >  binsulin-seq-clean.txt
binsulin=$(cat binsulin-seq-clean.txt)
# echo "$binsulin"

grep -o '[a-z]' preproinsulin-seq-clean.txt | tr -d '\n' | cut -c55-89 > cinsulin-seq-clean.txt
cinsulin=$(cat cinsulin-seq-clean.txt)
# echo "$cinsulin"

grep -o '[a-z]' preproinsulin-seq-clean.txt | tr -d '\n' | cut -c90-110 >  ainsulin-seq-clean.txt
ainsulin=$(cat ainsulin-seq-clean.txt)
# echo "$ainsulin"

insulin="${binsulin}${ainsulin}"
# echo "$insulin"

python3 insulin_analysis.py "$preproinsulin" "$isinsulin" "$binsulin" "$cinsulin" "$ainsulin" "$insulin"
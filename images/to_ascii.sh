#!/bin/bash
#run sh to_ascii.sh
for f in "THE LAB.png"; do
img2txt art ascii "$f" -W 100 -f ./100/"${f%.*}" -q
echo ${f%.*}
done

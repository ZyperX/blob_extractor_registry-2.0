#!/bin/bash
rm -rf *.gzip
for i in $(cat blobs.txt);do
 echo "Downloading blobs:"$i""
 curl --silent -u admin:admin -k https://docker.registry.htb/v2/bolt-image/blobs/$i --output $i.gz
done

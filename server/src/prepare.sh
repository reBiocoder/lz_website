#!/bin/bash

if [ -L ./Homologs ] ; then
  cd Homologs
else
  ln -s /home/xiaoming/Homologs/ ./Homologs
  cd Homologs
fi

currentTimeStamp=`date +%s`

sudo bash Extra_BlastP_parse.sh $1 $currentTimeStamp
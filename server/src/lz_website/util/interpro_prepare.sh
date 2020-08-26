#!/bin/bash

if [ -L ./Interpro ] ; then
  cd Interpro
else
  ln -s /home/xiaoming/Interpro/ ./Interpro
  cd Interpro
fi

sudo bash unzip_by_locustag.sh $1 $2
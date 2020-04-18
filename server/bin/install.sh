#!/usr/bin/env bash

venv_switch='on' # on/off

os_name=$(uname)
if [[ "$os_name" == 'Linux' ]]; then
   get_path=readlink
elif [[ "$os_name" == 'Darwin' ]]; then
   get_path=greadlink
fi

work_dir=$(dirname $(dirname $($get_path -f $0)))
for file in ${work_dir}/src/*
do [ -d $file ] && { app_name=${file##*/}; break; } done

cd $work_dir

major=$(python -c 'import sys; print(sys.version_info.major)')
minor=$(python -c 'import sys; print(sys.version_info.minor)')
if [[ $major -ne 3 || $minor -ne 6 ]]; then
    echo "python version error, python3.6 is required"
    exit -1
fi

if [ ! -f .already_package ]; then
    echo "can not install without packaging"
    exit -1
fi

if [ ! -d  ~/.pip ]; then
    mkdir ~/.pip
    touch ~/.pip/pip.conf
    echo '[global]' >> ~/.pip/pip.conf
    echo 'index-url = https://pypi.tuna.tsinghua.edu.cn/simple' >> ~/.pip/pip.conf
fi

if [[ "$venv_switch" == 'on' ]]; then
    [ -d env ] && rm -rf env
    virtualenv -p python env
    if [ $? -ne 0 ]; then
        echo "virtualenv error, installing interrupt"
        exit -1
    fi
    source env/bin/activate
fi

whl_count=$(ls lib | grep -i '^mg_app_framework.*whl$' | wc -l)
if [[ "$whl_count" != 1 ]]; then
    echo "pip install error, mg_app_framework.*whl count != 1"
    exit -1
fi

for item in $(ls lib/*.whl);do
    python -m pip install $item
    if [ $? -ne 0 ]; then
        echo "pip install error, installing interrupt"
        exit -1
    fi
done
for item in $(cat ./lib/requirements.txt);do
    python -m pip install $item
    if [ $? -ne 0 ]; then
        echo "pip install error, installing interrupt"
        exit -1
    fi
done

if [[ ! -f /etc/rc.local ]]; then
    touch /etc/rc.local
    chmod a+x /etc/rc.local
fi

rclocal_last_line=$(tail -n 1 /etc/rc.local)
if [[ $rclocal_last_line == *"exit 0"* ]]; then
    sed -i "/$app_name/d" /etc/rc.local
    sed -i "\$i $work_dir/bin/run.sh start" /etc/rc.local
else
    echo '#!/bin/bash' >> /etc/rc.local
    start_cmd="$work_dir/bin/run.sh start"
    echo "$start_cmd" >> /etc/rc.local
    echo 'exit 0' >> /etc/rc.local
fi

chmod u+x ./bin/run.sh

logstash_path="/etc/logstash/manugence/"

temp_logstash_conf_name=${work_dir//_/-}
logstash_conf_name=${temp_logstash_conf_name////_}

app_log_url=$work_dir"/log/*"
flag=False

if [[ ! -d $logstash_path ]]; then
    echo 'error: system missing logstash'
    flag=True
else
	for file in $logstash_path'*'
	do
	    if cat $file | grep "$app_log_url">/dev/null
        then
            echo 'info: app_log_url already configured'
            flag=True
            break
        fi
	done
fi

if [ $flag == False ]
then
    logstash_filename_path=${logstash_path}${logstash_conf_name}
    touch $logstash_filename_path

    echo 'input{
      file{
            path => "'${app_log_url}'"
            start_position => "beginning"
        }
    }' > $logstash_filename_path
fi

touch .already_install
echo 'info: finish'
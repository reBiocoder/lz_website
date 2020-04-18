#!/usr/bin/env bash

debug_switch='off' # on/off
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

process_info="ps aux | grep src/run_${app_name}.py | grep -v grep"
pid_file=".${app_name}_pid"

start() {
    cd $work_dir
    if [ ! -f .already_install ]; then
        echo "can not start without installing"
        return 1
    fi
    if [[ "$venv_switch" == 'on' ]]; then
        source env/bin/activate
    fi
    if [ -f $pid_file ]; then
        pid=$(cat $pid_file)
        process=$(eval "ps -p ${pid} | sed 1d")
        if [ -n "$process" ]; then
            echo "error: ${app_name}(pid=${pid}) is already running."
            return 1
        else
            rm $pid_file
        fi
    fi
    service=$(eval $process_info)
    if [ -n "$service" ]; then
        echo "info: a running ${app_name} instance exists."
    fi
    if [[ "$debug_switch" == 'off' ]]; then
        nohup python "./src/run_${app_name}.py" product >/dev/null 2>&1 &
    elif [[ "$debug_switch" == 'on' ]]; then
        python "./src/run_${app_name}.py"
    fi
    echo $! > $pid_file
    sleep 1
    pid=$(cat $pid_file)
    process=$(eval "ps -p ${pid} | sed 1d")
    if [ -n "$process" ]; then
    	echo "info: ${app_name}(pid=${pid}) started."
        return 0
    else
        echo "error: ${app_name} starting failed"
	    return 1
    fi
}

stop() {
    cd $work_dir
    service=$(eval $process_info)
    if [ -z "$service" ]; then
    	[ -f $pid_file ] && rm $pid_file
        echo "info: ${app_name} is not running."
        return 1
    else
    	if [ ! -f $pid_file ]; then
            echo "error: $(pwd)/${pid_file} not found, please kill by hand"
	        return 1
    	fi
    fi
    pid=$(cat $pid_file)
    for i in {1..5}; do
    	kill -9 $pid && sleep $i
        process=$(eval "ps -p ${pid} | sed 1d")
        if [ -z "$process" ]; then
            rm $pid_file
	        echo "info: ${app_name}(pid=${pid}) stopped."
            return 0
        fi
    done
    echo "error: ${app_name}(pid=${pid}) stopping failed"
    return 1
}

status() {
    cd $work_dir
    if [ -f $pid_file ]; then
        pid=$(cat $pid_file)
        process=$(eval "ps -p ${pid} | sed 1d")
        if [ -n "$process" ]; then
            echo "${app_name}(pid=${pid}) is running."
        else
            rm $pid_file
            echo "${app_name}(pid=${pid}) is not running"
        fi
    else
	    echo "${app_name} is not running"
    fi
    return 0
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart)
    stop
    start
    ;;
  status)
    status
    ;;
  *)
    echo "usage: run.sh {start|stop|restart|status}"
    exit 1
esac

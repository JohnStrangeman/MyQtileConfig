#!/bin/bash

option1=" logout"
option2=" reboot"
option3=" power off"

options="$option1\n$option2\n$option3\n"

choice=$(echo -e $options | rofi -dmenu)

case $choice in
	$option1)
		qtile cmd-obj -o cmd -f shutdown ;;
	$option2)
		reboot ;;
	$option3)
		shutdown now ;;
esac


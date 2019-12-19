#!/bin/sh

xprop -root _NET_ACTIVE_WINDOW | awk ' { print $5 } '

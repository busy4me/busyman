#!/usr/bin/env bash
# getwindidbypid
# 
# Get the ID of a window by PID (if the process has a window).
# 
# Usage:
#   getwindidbypid <PID>
# 

while IFS= read line; do
  if [[ "${line}" =~ (0x)([0-9a-z]+)([ ][- ][0-9]+[ ])([0-9]*) ]]; then
    winId="${BASH_REMATCH[1]}${BASH_REMATCH[2]}"
    pid="${BASH_REMATCH[4]}"
    if [[ "${pid}" -eq "${1}" ]]; then
      WIND_IDS+=("${winId}")
    fi
  fi
done < <(wmctrl -lp)

if [ "${#WIND_IDS[@]}" -gt 0 ]; then
  echo "${WIND_IDS[@]}"
fi
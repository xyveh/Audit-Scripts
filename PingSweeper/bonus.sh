#!/bin/bash
# File:        bonus.sh
# Author:      Oshada Palitharathna - ATHENA GROUP

banner() {
clear
printf " \e[91m      /\      \e[0m\e[1;92m  --------   \e[0m\e[1;93m  __     __  \e[0m\e[1;94m  _______  \e[0m\e[1;95m  ___      __  \e[0m\e[1;96m      /\       \e[0m\n"
printf " \e[91m     /  \     \e[0m\e[1;92m |__    __|  \e[0m\e[1;93m |  |   |  | \e[0m\e[1;94m |  _____| \e[0m\e[1;95m |    \   |  | \e[0m\e[1;96m     /  \      \e[0m\n"
printf " \e[91m    / /\ \    \e[0m\e[1;92m    |  |     \e[0m\e[1;93m |  |___|  | \e[0m\e[1;94m |  |___   \e[0m\e[1;95m |  |\ \  |  | \e[0m\e[1;96m    / /\ \     \e[0m\n"
printf " \e[91m   / /__\ \   \e[0m\e[1;92m    |  |     \e[0m\e[1;93m |   ___   | \e[0m\e[1;94m |  ____|  \e[0m\e[1;95m |  | \ \ |  | \e[0m\e[1;96m   / /__\ \    \e[0m\n"
printf " \e[91m  / ______ \  \e[0m\e[1;92m    |  |     \e[0m\e[1;93m |  |   |  | \e[0m\e[1;94m |  |____  \e[0m\e[1;95m |  |  \ \|  | \e[0m\e[1;96m  / ______ \   \e[0m\n"
printf " \e[91m /_/      \_\ \e[0m\e[1;92m    |__|     \e[0m\e[1;93m |__|   |__| \e[0m\e[1;94m |_______| \e[0m\e[1;95m |__|   \____| \e[0m\e[1;96m /_/      \_\  \e[0m\e[40;38;5;82mCSEC\e[30;48;5;82m472\e[0m\n"
printf " \e[45m ROCHESTER INSTITUTE OF TECHNOLOGY - DUBAI \e[0m\n"
printf " \n"
}

bonus() {
  printf "\e[42m Please enter the subnet: \e[0m\n"
  read SUBNET
  echo " "
  printf "#############################\n"
  printf "#### Starting Ping Sweep ####\n"
  printf "#############################\n"
  echo " "

  for IP in $(seq  1 254); do
      ping -c 1 $SUBNET.$IP | tr \\n ' ' | awk '/1 packets received/ {printf "The host " $2 " is active"}';
  done
}

banner
bonus

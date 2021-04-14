[Unit]
Description=A service to check current name day

[Service]
ExecStart =/usr/bin/python3.8 /c/Workspace/PythonProject1/main.py

[Install]
WantedBy = multi - user.target

#För att göra detta till en service kör man(mv name_day.service /lib/systemd/system/name_day.service)
#Och för att kolla om servicen har kommit dit kan man göra en systemctl status name_day.service
#Är den inte startad så kör man systemctl start name_day.service
# SSH a Network device(Huawei S5720) by Paramiko in Python

We need bulid a environment to connect the device and the host that running the python.

## 1.configure connectivity

I have a Huawei S5720 Ethernet Switch,I will connect it by my console line and i'll write codes in my laptop.

configure S5720:

    <Quidway>sys
    [Quidway]int vlan1
    [Quidway]ip add 1.1.1.1 24
    [Quidway]quit

Test connectivity:

    <Quidway>ping -a 1.1.1.1 1.1.1.2
      PING 1.1.1.2: 56  data bytes, press CTRL_C to break
        Reply from 1.1.1.2: bytes=56 Sequence=1 ttl=128 time=1 ms
        Reply from 1.1.1.2: bytes=56 Sequence=2 ttl=128 time=1 ms
        Reply from 1.1.1.2: bytes=56 Sequence=3 ttl=128 time=1 ms
        Reply from 1.1.1.2: bytes=56 Sequence=4 ttl=128 time=1 ms
        Reply from 1.1.1.2: bytes=56 Sequence=5 ttl=128 time=1 ms

      --- 1.1.1.2 ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 1/1/1 ms

The ip 1.1.1.2 is my laptop address.
## 2.configure SSH
```
[Quidway]stelnet server enable 
[Quidway]user-interface vty 0 4
[Quidway-ui-vty0-4]authentication-mode aaa
[Quidway-ui-vty0-4]protocol inbound ssh
[Quidway-ui-vty0-4]user privilege level 15
[Quidway-ui-vty0-4]quit
[Quidway]aaa
[Quidway-aaa]local-user makinami password irreversible-cipher ayanami2022
[Quidway-aaa]local-user makinami service-type ssh
[Quidway-aaa]quit
[Quidway]ssh user makinami
[Quidway]ssh user makinami service-type stelnet 
```
## 3.configure python codes to connect network device
running SSH.py
the content is as follows:
```
Info: The max number of VTY users is 10, and the number
      of current VTY users on line is 1.
      The current login time is 2000-04-02 00:55:23+08:00.
<Quidway>display version
Huawei Versatile Routing Platform Software
VRP (R) software, Version 5.170 (S5720 V200R010C00SPC600)
Copyright (C) 2000-2016 HUAWEI TECH CO., LTD
HUAWEI S5720-28P-PWR-LI-AC Routing Switch uptime is 0 week, 0 day, 1 hour, 0 minute

ES5D2V28S006 0(Master)  : uptime is 0 week, 0 day, 0 hour, 59 minutes
DDR    Memory Size      : 512        M bytes
FLASH  Memory Size      : 238        M bytes
Pcb           Version   : VER.A
BootROM       Version   : 020a.0001
BootLoad      Version   : 020a.0001
CPLD          Version   : 0106 
Software      Version   : VRP (R) Software, Version 5.170 (V200R010C00SPC600)
<Quidway>
```

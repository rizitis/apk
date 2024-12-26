# apk
**emulation** of apk package manager **commands** on a slackware system for the specific repository **only** and for slackware**64-current**

## ?
Personal and *unofficial* binary repository with its own Package Manager, for Slackware64-current.<br>
It is tradition almost every *unofficial* Slackware repository to have its own package manager, so here is mine which work only with this repository **of course** :D


### !
This is not apk-tools (Alpine Package Keeper) or  Chimera`s next-generation version 3.<br>
This apk is a simple bash script which was written from scratch to work exclusively with this repository. 

#### %
- Dependencies: None in full Slackware installation. Else:`"bash curl pkgtools"`
- To install apk (meaning the package manager):
  - As regular user command: `mkdir -p /tmp/apk && cd /tmp/apk || exit && curl -L -O https://raw.githubusercontent.com/rizitis/apk/refs/heads/main/apk && curl -L -O https://raw.githubusercontent.com/rizitis/apk/refs/heads/main/apk.env`
  - Then be root (su -l) and command: `cd /tmp/apk || exit && mkdir -p /etc/apk && cp ./apk.env /etc/apk/ && cp ./apk /usr/local/sbin/ && chmod +x /usr/local/sbin/apk`
  - Finally always as root run the update command: `apk update` to connect apk with remote packages repository.
- HowTo use it always as root command: `apk --help`
- To uninstall as root: `rm -rf /etc/apk /usr/share/apk /usr/local/sbin/apk /usr/lib/apk` 

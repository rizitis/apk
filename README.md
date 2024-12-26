# apk
**emulation** of apk package manager **commands** on a slackware system for the specific repository **only** and for slackware**64-current**

---

## ?
Personal and *unofficial* binary repository with its own Package Manager, for Slackware64-current.<br>
It is tradition almost every *unofficial* Slackware repository to have its own package manager, so here is mine which work only with this repository **of course** :D

---

### !
This is not apk-tools (Alpine Package Keeper) or  Chimera`s next-generation version 3.<br>
This apk is a simple bash script which was written from scratch to work exclusively with this repository. 

---

#### %
- Dependencies: None in full Slackware installation. Else:`"bash curl pkgtools"`
- To install apk (meaning the package manager):
  - As regular user paste in terminal all this ugly cmd line: `mkdir /tmp/apk && cd /tmp/apk || exit && curl -L -O https://raw.githubusercontent.com/rizitis/apk/refs/heads/main/apk && curl -L -O https://raw.githubusercontent.com/rizitis/apk/refs/heads/main/apk.env`
  - Then be root (su -l) and command: `cd /tmp/apk || exit && mkdir -p /etc/apk && cp ./apk.env /etc/apk/ && cp ./apk /usr/local/sbin/ && chmod +x /usr/local/sbin/apk`
  - Finally always as root run the update command 2 times: `apk update` to connect apk with remote repository and again `apk update` to update pakcages lists.
  - To blacklist packages for slackpkg, as root: `echo "[0-9]+_rtz" >> /etc/slackpkg/blacklist`
- HowTo use apk, always as root command: `apk --help`
```
# === Commands for  Download,Install,Upgrade,Remove,Search <packages> === #
    #
    # apk add pkg       Add/Install a package
    # apk del pkg       Delete a package
    # apk search pkg    Search for packages
    # apk fix pkg       Repair package or Upgrade it without modifying dependencies
    # apk download pkg  Download package files but not install
    #
    # === Commands which not followed by <package> === #
    #
    # apk update        Update apk repository {local files and package list}.
    # apk upgrade       Upgrade all installed packages from the apk repository ONLY.
    # apk info          List all installed packages from the apk repository ONLY.
    # apk stats         Show statistics ONLY about apk repository and installations.
    # apk upgrade-apk   Upgrade apk script version and apk.env.
    # apk restore-apk   downgrade apk script and apk.env to previous status before upgrade-apk.
    # apk help          Print help message
```
- To uninstall apk, as root: `rm -rf /etc/apk /usr/share/apk /usr/local/sbin/apk /usr/lib/apk` 

---

#### @#$^!
Stop screaming and open an issue:<br>
https://github.com/rizitis/apk/issues<br>
With God`s help maybe we can fix it...

---

#### *
Note: *this is not SBo/ponce or conraid or alienbob repos<br>
I m just having fun here and build packages I need and **not exist** there most of times.<br>
If Slackware-stable was released every year and not when its ready, probably all these packages should be in SBo by me.<br>
But now most of them do not run or build properly in Slackware-stable so they will not be accepted in SBo<br>
Thats all, happy slacking...* 

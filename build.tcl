#!/usr/bin/tclsh

set arch "x86_64"
set base "tkzinc-3.3.6"
set fileurl "https://bitbucket.org/plecoanet/tkzinc/get/4c4937fcff4b.zip"

set var [list wget $fileurl -O tkzinc.zip]
exec >@stdout 2>@stderr {*}$var

set var [list unzip tkzinc.zip]
exec >@stdout 2>@stderr {*}$var

set curDir [pwd]

file rename plecoanet-tkzinc-4c4937fcff4b $base

set var [list tar czvf $base.tar.gz $base]
exec >@stdout 2>@stderr {*}$var

# Remove old file
file delete -force tkzinc.zip

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force PostScript.c.patch build/SOURCES
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcl-tkzinc.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete $base.tar.gz

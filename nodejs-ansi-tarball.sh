#!/bin/sh

if [ $# -eq 1 ]; then
    version="${1}"
else
    version=$(rpm -q --specfile --qf='%{version}' nodejs-ansi.spec)
fi
wget http://registry.npmjs.org/ansi/-/ansi-${version}.tgz
tar -zxf ansi-${version}.tgz
rm -f package/examples/imgcat/yoshi.png
tar -zcf ansi-${version}-stripped.tgz package

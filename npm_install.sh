#!/usr/bin/env bash
#
# Use a single node_modules directory for all tox envs.
# Either copy or link the node_modules cache.

set -o errexit
set -o nounset
set -o pipefail

E_NOARGS=75
NODE_CACHE=../../node_cache
TOXTMP=$(pwd)

function usage {
    echo "Usage: `basename ${0}` [copy | link]"
    exit ${E_NOARGS}
}

if [ $# -lt 1 ]; then
    usage
fi

case $1 in
    copy) CMD="cp -R";;
    link) CMD="ln -s";;
    *) usage;;
esac

if [ ! -d ${NODE_CACHE} ]; then
    mkdir ${NODE_CACHE}
    cp my-project/package.json ${NODE_CACHE}
    cd ${NODE_CACHE}
    npm install
fi

cd ${TOXTMP}/my-project
${CMD} ../${NODE_CACHE}/node_modules .

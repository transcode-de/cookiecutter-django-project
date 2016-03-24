#!/usr/bin/env bash
#
# Use a single node_modules directory for all tox envs.

set -o errexit
set -o nounset
set -o pipefail

NODE_CACHE=../../node_cache
TOXTMP=$(pwd)

if [ ! -d ${NODE_CACHE} ]; then
    mkdir ${NODE_CACHE}
    cp my-project/package.json ${NODE_CACHE}
    cd ${NODE_CACHE}
    npm install
fi

cd ${TOXTMP}/my-project
ln -fs ../${NODE_CACHE}/node_modules

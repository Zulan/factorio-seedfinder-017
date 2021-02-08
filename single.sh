#!/usr/bin/env bash

F=$PWD/factorio/bin/x64/factorio
SETTINGS=$PWD/settings.json

# Convert "min max" as one string argument
ARR=($1)
MIN=${ARR[0]}
MAX=${ARR[1]}
SLOT=$2
DIR="local/$SLOT"

if [ ! -d "$DIR" ]; then
    mkdir -p $DIR
    sed -e "s/NNNNNN/${SLOT}/g" ./config.ini.tmpl > $DIR/config.ini
fi

$F -c $DIR/config.ini                                              \
   --map-gen-settings $SETTINGS                                    \
   --map-preview-size $((32 * 8 / 8))                             \
   --map-preview-scale 8                                           \
   --generate-map-preview /dev/null/                               \
   --map-gen-seed $MIN --map-gen-seed-max $MAX                     \
   --report-quantities iron-ore,copper-ore                         \
   | $PWD/filter.py

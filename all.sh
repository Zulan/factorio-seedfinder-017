#!/usr/bin/env bash

#./make_seed_chunks | parallel --results ./results --joblog ./joblog ./single.sh {}
parallel -a ./test.in --progress --results ./results --joblog ./joblog ./single.sh {} {%}

#!/usr/bin/env python3

chunk_size = 10000
for seed_min in range(1, 2**32-2, chunk_size):
    seed_max = seed_min + chunk_size
    seed_max = min(seed_max, 2**32-1)
    print(f"{seed_min} {seed_max}")
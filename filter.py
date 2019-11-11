#!/usr/bin/env python3
import csv
import re
import sys


#    0.597 Generating map preview: 1600 pixels: -160.000000,-160.000000...160.000000,160.000000; 8.000000 meters per pixel
#    0.656 Approximate quantities of resources on this map:
#    0.656 copper-ore: total:393866.95, averageQuantity:3.8464, maxUnclampedProbability:1.0000, maxRichness:2117.2349, averageRichness:879.1673
#    0.656 iron-ore: total:184095.99, averageQuantity:1.7978, maxUnclampedProbability:1.0000, maxRichness:897.6458, averageRichness:319.6111
#    0.656 Map preview generation time: 0.059155 seconds.
#    0.666 Error MapPreviewGenerator.cpp:400: Thread failed: Error when opening /dev/null/1.png for writing: Not a directory.

class Filter:
    def __init__(self, entities):
        self._counts = {}
        self._entities = entities
        self._writer = None

    def count(self, entity, cnt):
        self._counts[entity] = cnt

    def collect(self, seed):
        if all([self._counts[entity] >= min_count for entity, min_count in self._entities.items()]):
            if self._writer is None:
                self._writer = csv.DictWriter(sys.stdout, ['seed'] + list(self._entities.keys()))
                self._writer.writeheader()
            self._counts['seed'] = seed
            self._writer.writerow(self._counts)

    def __call__(self, line):
        n = r'\d*\.\d*'
        m = re.search(f'{n} ([^:]+): total:({n}), averageQuantity:{n}, maxUnclampedProbability:{n}, maxRichness:{n}, averageRichness:({n})', line)
        if m:
            self.count(m.group(1), float(m.group(2)) / float(m.group(3)))
        m = re.search(f'{n} Error MapPreviewGenerator.cpp:\d+: Thread failed: Error when opening /dev/null/(\d+).png for writing: Not a directory', line)
        if m:
            self.collect(int(m.group(1)))


def main():
    flt = Filter({'iron-ore': 8000, 'copper-ore': 6000})
    for line in sys.stdin:
        flt(line)


if __name__ == '__main__':
    main()
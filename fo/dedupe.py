import os
import hashlib


class DedupeCommand:
    NAME = "dedupe"
    HELP = "Dedupe files"

    _CHUNK_NUM_BLOCKS = 128

    def prepare(self, parser):
        parser.add_argument("source")

    def execute(self, args):
        working_directory = os.path.abspath(args.source)
        self._traverse(working_directory)

    def _traverse(self, directory):
        print(f"Deduping '{directory}'...\n")
        checksums = set()
        for entry in self._get_entry(directory):
            md5 = self._get_checksum(entry.path)
            if md5 in checksums:
                print(f"Removing dupe '{entry.name}")
                os.remove(entry.path)
            else:
                checksums.add(md5)
                print(f"Unique: '{entry.name}")

    def _get_entry(self, directory):
        for entry in os.scandir(directory):
            if entry.name not in ['.', '..'] and not entry.is_dir():
                yield entry

    def _get_checksum(self, file):
        h = hashlib.md5()
        with open(file, 'rb') as f:
            while chunk := f.read(self._CHUNK_NUM_BLOCKS * h.block_size):
                h.update(chunk)
        return h.digest()

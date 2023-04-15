#!/usr/bin/env python3

import argparse
import subprocess
import sys
import os

VIDEO_FILE_EXTENSIONS = ["avi", "mp4", ""]
IMAGE_FILE_EXTENSIONS = ["avif", "gif", "heic",
                         "heif", "hif", "jpeg", "jpg", "jpe", "png", "jng",
                         "mng", "thm"]
AUDIO_FILE_EXTENSIONS = ["mp3", "flac", "flv", "wav"]
DOCUMENT_FILE_EXTENSIONS = ["doc", "docx", "epub",
                            "pdf", "txt", "xls", "xlt", "xlsx", "xlsm", "xlsb"]
TRASH_FILE_EXTENSIONS = ["json", "js", "java", "c",
                         "h", "idx", "pack", "yml", "markdown", "md", "sample", "tex", "aux"]

MEMORY_FILE_EXTENSIONS = VIDEO_FILE_EXTENSIONS + IMAGE_FILE_EXTENSIONS


def to_lower(filename: str) -> str:
    return ""


def with_hyphens(filename: str) -> str:
    return ""


def get_extension(filename: str) -> str:
    return ""


def is_memory(extension: str) -> bool:
    return extension in MEMORY_FILE_EXTENSIONS


def is_document(extension: str) -> bool:
    return extension in DOCUMENT_FILE_EXTENSIONS


def is_trash(extension: str) -> bool:
    return extension in TRASH_FILE_EXTENSIONS


# Check for dotfile as well, e.g. ".gitignore"
def has_extension(filename: str) -> bool:
    return not filename.startswith(".") and "." in filename


TRANSFORMATIONS = [to_lower, with_hyphens]

# Move files into folders by categories
class CategorizeCommand:
    NAME = "categorize"
    HELP = "Categorize files"

    def prepare(self, parser):
        parser.add_argument("--source", required=True)
        parser.add_argument("--memories", required=True)

    def execute(self, args):
        print(args)

import argparse
import os
import json

from compile import *
from link import *
from preprocess import *

sources = {}
output = "a"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aqua compiler")
    
    parser.add_argument("-s", "--sources", nargs='+', help='Sources to compile', required=True)
    parser.add_argument("-o", "--output", type=str, help='Output directory')
    
    parser.add_argument("-p", "--preprocess", action='store_true', help="Stop compiler after preprocess")
    parser.add_argument("-c", "--compile", action='store_true', help="Stop compiler after compile")
    
    args = parser.parse_args()
import argparse
import os
import time

from lz77 import LZ77Compressor

compressor = LZ77Compressor(window_size=20)  # window_size is optional


parser = argparse.ArgumentParser(description="LZ77 Algorithm for Compression and Decompression",
                                 usage="mainlz77.py [action] FilePath")

parser.add_argument("-c", "--compress", type=str, help="compress")
parser.add_argument("-d", "--decompress", type=str, help="decompress")

args = parser.parse_args()


if args.compress:
    filepath = args.compress
    input_file_path = filepath
    output_file_path = filepath + '.lz77'

    t1 = time.time()
    # compress the input file and write it as binary into the output file
    compressor.compress(input_file_path, output_file_path)
    t2 = time.time()
    exec_time = t2 - t1

    input_size = os.stat(input_file_path).st_size
    output_size = os.stat(output_file_path).st_size
    ratio = output_size * 100 / input_size

    print("[+] %s : created successfully." % output_file_path)
    print("[+] Compression ratio  %.1f" % ratio)
    print("[+] Compression finished in %.5f seconds" % exec_time)


elif args.decompress:
    filepath = args.decompress
    input_file_path = filepath + '.lz77'
    output_file_path = filepath + '.lz77decoded'

    t1 = time.time()
    # decompress the input file and write it as binary into the output file
    compressor.decompress(input_file_path, output_file_path)
    t2 = time.time()

    exec_time = t2 - t1
    print("[+] Decompression finished in %.5f seconds" % exec_time)


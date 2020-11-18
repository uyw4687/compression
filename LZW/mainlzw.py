import lzw
import argparse
import os
import time

buffersize = 1024

parser = argparse.ArgumentParser(description="LZW Algorithm for Compression and Decompression",
                                 usage="mainlzw.py [action] FilePath")

parser.add_argument("-c", "--compress", type=str, help="compress")
parser.add_argument("-d", "--decompress", type=str, help="decompress")

args = parser.parse_args()


if args.compress:
    filepath = args.compress
    input_file_path = filepath
    output_file_path = filepath + '.lzw'

    t1 = time.time()
    compressed = lzw.compress(lzw.readbytes(input_file_path))
    lzw.writebytes(output_file_path, compressed)
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
    input_file_path = filepath + '.lzw'
    output_file_path = filepath + '.lzwdecoded'

    t1 = time.time()
    uncompressed = lzw.decompress(lzw.readbytes(input_file_path, buffersize))
    lzw.writebytes(output_file_path, uncompressed)
    t2 = time.time()

    exec_time = t2 - t1
    print("[+] Decompression finished in %.5f seconds" % exec_time)


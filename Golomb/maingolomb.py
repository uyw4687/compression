import golomb
import argparse
import os

mGolomb = 1024

parser = argparse.ArgumentParser(description="Golomb Algorithm for Compression and Decompression",
                                 usage="maingolomb.py [action] FilePath")

parser.add_argument("-c", "--compress", type=str, help="compress")
parser.add_argument("-d", "--decompress", type=str, help="decompress")

args = parser.parse_args()


if args.compress:
    filepath = args.compress
    input_file_path = filepath
    output_file_path = filepath + '.golomb'

    exec_time = golomb.compress(input_file_path, output_file_path, mGolomb)

    input_size = os.stat(input_file_path).st_size
    output_size = os.stat(output_file_path).st_size
    ratio = output_size * 100 / input_size

    print("[+] %s : created successfully." % output_file_path)
    print("[+] Compression ratio  %.1f" % ratio)
    print("[+] Compression finished in %.5f seconds" % exec_time)


elif args.decompress:
    filepath = args.decompress
    input_file_path = filepath + '.golomb'
    output_file_path = filepath + '.golombdecoded'

    exec_time = golomb.decompress(input_file_path, output_file_path, mGolomb)

    print("[+] Decompression finished in %.5f seconds" % exec_time)


import hashlib

input_file_path = "C:\\Users\\ata.erdemir\\Desktop\\Global Scanners.txt"
output_file_path = "C:\\Users\\ata.erdemir\\Desktop\\guncel.txt"

completed_lines_hash = set()
output_file = open(output_file_path, "w")

for line in open(input_file_path, "r"):
    hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

    if hashValue not in completed_lines_hash:
        output_file.write(line)
        completed_lines_hash.add(hashValue)

output_file.close()


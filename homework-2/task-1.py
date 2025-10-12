def copy_file(src, dst):
    with open(src, 'r') as f_src:
        with open(dst, 'w') as f_dst:
            f_dst.write(f_src.read())

copy_file('homework-2/source.txt', 'homework-2/destination.txt')
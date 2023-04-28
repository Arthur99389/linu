import subprocess
import zlib


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def crc32(b, s):
    h_crc = zlib.crc32(b'path_arch')
    return h_crc

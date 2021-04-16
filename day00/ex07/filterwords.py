import sys
import re
if (len(sys.argv) == 3) and not sys.argv[1].isdigit():
    try:
        nb = int(sys.argv[2])
    except:
        sys.exit("ERROR")
    filt = re.findall(r"[\w']+", sys.argv[1])
    print([i for i in filt if len(i) > nb])
else:
    sys.exit("ERROR")
import sys
import string
import time
sys.path.append('../')

from huahuacaocao import HuaHuaCaoCao

hhcc = HuaHuaCaoCao()

pids = []
for char in string.ascii_lowercase:
    count = 0
    success = True

    while success:
        try:
            print ('char "%s" at %s' % (char, count))
            sys.stdout.flush()

            response = hhcc.find_plant_by_alias(char, count)

            if response['status'] == 100 and response['description'] == 'done':
                pids.extend([plant['pid'] for plant in response['data']])
                count += 20
            else:
                success = False
        except Exception as e:
            print(e)
            time.sleep(10)

print(set(pids))
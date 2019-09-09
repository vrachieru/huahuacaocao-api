import sys
import json
sys.path.append('../')

from huahuacaocao import HuaHuaCaoCao

hhcc = HuaHuaCaoCao()
json.dump(hhcc.get_plant_details('carmona microphylla'), sys.stdout, indent=4)

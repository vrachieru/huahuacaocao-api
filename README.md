<p align="center">
    <img src="https://user-images.githubusercontent.com/5860071/64519445-caf29d80-d2fc-11e9-8f08-d7b4d5037a1b.png" width="70px" />
    <br/>
    <a href="https://github.com/vrachieru/huahuacaocao-api/releases/latest">
        <img src="https://img.shields.io/badge/version-1.0.0-brightgreen.svg?style=flat-square" alt="Version">
    </a>
    <a href="https://travis-ci.org/vrachieru/huahuacaocao-api">
        <img src="https://img.shields.io/travis/vrachieru/huahuacaocao-api.svg?style=flat-square" alt="Version">
    </a>
    <br/>
    HuaHuaCaoCao (Xiaomi Flower Care) API wrapper
</p>

## Features

* Find plant by name
* Get plant description and care information

## Install

```bash
$ pip3 install git+https://github.com/vrachieru/huahuacaocao-api.git
```
or
```bash
$ git clone https://github.com/vrachieru/huahuacaocao-api.git
$ pip3 install ./huahuacaocao-api
```

## Usage

### Get plant information

```python
import json
import huahuacaocao

hhcc = huahuacaocao.HuaHuaCaoCao()

json.dump(hhcc.get_plant_details('carmona microphylla'), sys.stdout, indent=4)
```

```bash
$ python3 plant_details.py

{
    "pid": "carmona microphylla",
    "basic": {
        "floral_language": "",
        "origin": "Tropical areas",
        "production": "China",
        "category": "Boraginaceae, Carmona",
        "blooming": "Flowering period May-July, fruiting period August-October",
        "color": "Flower color white"
    },
    "display_pid": "Carmona microphylla",
    "maintenance": {
        "size": "Diameter \u2265 10 cm, height \u2265 10 cm",
        "soil": "Loose, fertile, and well-drained acid soil",
        "sunlight": "Like bright scattered sunlight, strong resistant to shade",
        "watering": "Water thoroughly when soil is dry, avoid saturated water",
        "fertilization": "Apply enough base fertilizers",
        "pruning": "Remove dead and diseased branches timely, strong ability to sprout"
    },
    "parameter": {
        "max_light_mmol": 5400,
        "min_light_mmol": 1800,
        "max_light_lux": 55000,
        "min_light_lux": 2000,
        "max_temp": 35,
        "min_temp": 5,
        "max_env_humid": 80,
        "min_env_humid": 30,
        "max_soil_moist": 60,
        "min_soil_moist": 20,
        "max_soil_ec": 2000,
        "min_soil_ec": 100
    },
    "image": "http://pkb.resource.huahuacaocao.com/Y2FybW9uYSBtaWNyb3BoeWxsYS5qcGc=?imageView2/1/w/%d/h/%d"
}
```

## License

MIT
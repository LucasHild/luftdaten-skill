# LufdatenSkill

A German Alexa Skill which can be used with a respirable dust sensor by [Luftdaten.info](https://luftdaten.info/).


[![](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/Lanseuo/luftdaten-skill/blob/master/LICENSE)
[![](https://img.shields.io/badge/alexa-skill-83bdfc.svg?style=flat-square)](https://www.amazon.de)

## Usage

**You:** Alexa, starte Feinstaubsensor.  
**Alexa:** Die Feinstaubbelastung in deiner Umgebung liegt aktuell bei 10,0 Mikrogramm.  
**You:** Richte meinen Sensor ein.  
**Alexa**: Wie lautet deine Sensor ID?  
**You:** 924  
**Alexa:** Perfekt, ab jetzt gebe ich Dir standardmäßig die Feinstaubwerte von deinem Sensor mit der ID 924 zurück.  

**You:** Alexa, starte Feinstaubsensor.  
**Alexa:** Die Feinstaubbelastung an deinem Sensor 924 liegt bei 10,0 Mikrogramm.

## Development

```bash
git clone https://github.com/Lanseuo/luftdaten-skill.git
cd luftdaten-skill
pip install -r requirements.txt
npm install
```

## Deployment

```bash
serverless deploy
```

## Meta

Lucas Hild - [https://lucas-hild.de](https://lucas-hild.de)  
This project is licensed under the MIT License - see the LICENSE file for details
# Pablito Vox Caster

*The dissident [invites](https://discordapp.com/oauth2/authorize?client_id=697772823044948019&permissions=2048&scope=bot) only retribution.*

A Only War discord bot.

![alt text](https://github.com/drblallo/PablitoVoxCaster/blob/master/pictures/examples/talent.png  "talent example")

## Usage:
currently pablito is able to:
* Return the thought of the day
  ```thought```
* Return crit damage table, with the command
  ```crit <type> <location> [level]```
* Return insanity table,with the comamnd
```ins [level]```
* Return all talents matching a string
```tal [name]```

## Collaborate:
It is really easy to improve Pablito, any improvement is well accepted. In particular it accepts tables in multiple formats, so even if you don't know python you can send us a table you would find usefull.

### Simple tables
Any file were each line is a entry of the table can be loaded.
As an example, a color table would be as simple as a txt file containing
```
red
blue
white
```

### Tiered Table
A table where each line is associated to a range [min, max] can be loaded if provided as a json file.
The json file must be a arry of object each with a text, a min and a max.
```json
[
	{
		"text": "long text",
		"min": 0,
		"max": 1
	},
	{
		"text": "long text again",
		"min": 2,
		"max": 20
	}
]
```
An example of such table is  the [insanity table](https://github.com/drblallo/PablitoVoxCaster/blob/master/tables/insanity.json)

### Talents:
Talents are provided as a json. It is composed by an array of object, each with the following fields:
* name : string
* tier : int
* prerequisites: string
* aptitute1: string
* aptitute2: string
* specializations: string
* effect: string
An example of such json is the [core rulebook json](https://github.com/drblallo/PablitoVoxCaster/blob/master/talents/talents.json)

### Other Games
We are open to support other games of the line as well, but we are not going to upload content until we are not going to play those games ourself.

If you want to send us material of each game we are happy to integrate it.

## Run your own instance:

### Ubuntu 18.04

#### Download
```bash
	git clone https://github.com/drblallo/PablitoVoxCaster
	cd PablitoVoxCaster/
	virtualenv --python=/usr/bin/python3 venv
	source venv/bin/activate.sh
	pip install requirements.txt
```

#### Configuration
Create a file called .env top level directory of the project.
Each line will be a key-value pair separated by a equal sign.
The current options are
* DISCORD_TOKEN=K 
	the token provided by discord when you create a new bot.
* DISCORD_PREFIX="#"
	the prefix used to invoke bot commands

### Run
```bash
	source venv/bin/activate.sh
	python PablitoVoxCaster.py
````
You should now see your instance of the bot, if you invited him correctly

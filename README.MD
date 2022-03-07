# Mapper - Count letter and Flatten nested dict


Console CLI app , mapping element inside string or file. The project currently supports:

  - Counting letter within a sentence.
  - Flatten nested dict from JSON file.

## Tech

Application is using following libraries:

* **Typer** - library for building CLI applications. Based on Python type hints.

## Installation

Once cloned on your local machine. Use to following commands to run the application.
```sh
$ cd mapper
$ python3 -m venv venv
```
Now the virtual env is all set. All you have to do is activate it.
Windows activation:

```sh
$ . venv/Scripts/activate
```
Linux:

```sh
$  source venv/bin/activate
```

Once activated navigate back to root directory and install all dependencies.

```sh
(venv) $ pip install -r requirements.txt
```


## Using the App

Inside this project there is mapper.py file which contains typer commands. That can be used to Count letter and Flatten nested dict.

Current typer commands:

* `python mapper.py -h` - show help section for application usage.

* `python mapper.py --letter-counter [STRING]`- count how many times every letter occurs in the passed `STRING`, and create a alphabetically sorted list with elements `<char>:<number of occurrences>`.

* `python mapper.py --parse-json-file [FILE_PATH]` - transform the content `FILE_PATH` into a dict and flatten it.


## Examples

>### Help Function
>```sh
>$ python mapper.py -h
>```
>
>usage: mapper.py [-h] [--letter-counter LETTERS] [--parse-json-file JSON_FILE]
>
>Task
>
>optional arguments:<br>
>-h, --help show this help message and exit<br>
>--letter-counter LETTERS<br>
>Counts every letter occurrence in a given string.<br>
>Returns sorted list<br>
>--parse-json-file JSON_FILE<br>
>Reads given JSON formatted file and outputs flatten DICT

>### Counting Letter
>```sh
>$ python mapper.py --letter-counter 'python syntax is very pretty'
>```
>
>[' :4', 'a:1', 'e:2', 'h:1', 'i:1', 'n:2', 'o:1', 'p:2', 'r:2', 's:2', 't:4', 'v:1', 'x:1', 'y:4']

>### Flatten Dict
>```sh
>$ python mapper.py --parse-json-file ./json-file.json
>```
>
>Nested dict: {'level1_key1': '1', 'level1_key2': {'level2_key1': '2', 'level2_key2': {'level3_key1': 'Congrats you have reached the maximum dept of the dict'}}}
>
>Flatten dict: {'level1_key1': '1', 'level2_key1': '2', 'level3_key1': 'Congrats you have reached the maximum dept of the dict'}
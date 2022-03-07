import typer
import json

APP_NAME = "Mapper"
app = typer.Typer(name=APP_NAME, add_completion=False)

def count_letter(sentence:dict):
    '''
    Iterate letter by letter in the sentence, then count it.
    '''
    letter_collections = {}
    for letter in sentence:
        if not letter in letter_collections:
            letter_collections[letter] = 0
        letter_collections[letter] += 1

    letter_list = []
    for key, value in letter_collections.items():
        letter_list.append(f"{key}:{value}")

    return sorted(letter_list)

def flatten_it(collection:dict, dict_source:dict):
    '''
    Convert nested dict into 1 dimension dict.
    '''
    for key, value in dict_source.items():
        if type(value) is dict:
            flatten_it(collection, value)
        else:
            collection[key] = value

@app.command()
def main_app(letter_counter: str = typer.Option(None, help="Counts every letter occurrence in a given string. Returns sorted list"),
        parse_json_file: typer.FileText = typer.Option(None, help="Reads given JSON formatted file and outputs flatten DICT"),
        help: bool = typer.Option(None, "--help", "-h", help="show this help message and exit") ):
    '''
    Mapper - Count letter and Flatten nested dict
    '''
    if help:
        typer.echo("usage: mapper.py [-h] [--letter-counter LETTERS] [--parse-json-file JSON_FILE]\n\nTask\n\n")
        typer.echo("optional arguments:")
        typer.echo("-h, --help show this help message and exit")
        typer.echo("--letter-counter LETTERS\nCounts every letter occurrence in a given string.\nReturns sorted list")
        typer.echo("--parse-json-file JSON_FILE\nReads given JSON formatted file and outputs flatten DICT")
        raise typer.Exit()

    if not letter_counter and not parse_json_file:
        typer.echo("Please use option '--letter-counter' or '--parse-json-file' detailed info please check help '-h'")
        raise typer.Abort()

    if letter_counter:
        typer.echo(count_letter(letter_counter))

    if parse_json_file:
        json_file = json.load(parse_json_file)
        typer.echo(f"Nested dict: {json_file}\n\n")

        flatten_dict = {}
        flatten_it(flatten_dict, json_file)
        typer.echo(f"Flatten dict: {flatten_dict}")


if __name__ == "__main__":
    app()

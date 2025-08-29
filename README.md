# wiki2md

This is a very simple python script with the purpose of converting from wiki format to markdown.

Why? I like writing in wiki format because it's nice, but approximately 3 people in the universe use it so I need markdown to share easily.

## Usage

```bash
python wiki2md.py [-h] [-o output_file.md] input_file.wiki
```

It's not that complicated, you always give an input and can use `-o` to specify
an optional ouutput file. If you don't give `-o` it writes to stdout.

## What is wiki format

It looks kinda like this

```text
= h1 =
== h2 ==
=== h3 ===
...
====== h6 ======

{{{python
def code_block(language):
    print(f'language is {language} in this code block :D')
}}}

_italics_ and *bold* happen within a line, and _*can be stacked*_ with each other.

[[links]] do not get converted by this script because I don't care about that.

`inline code` works the same no matter what, making `*other* _syntax_ _*not apply*_`
```

## Run an example

There's one in this repo.

```
$ python wiki2md.py example/input.wiki -o example/output.md
$ diff example/output.md example/expected.md
```

Woaaaw! The contrived example works!

If there are bugs I'll fix em if they actually matter to my use case otherwise this is feeling like too much energy.

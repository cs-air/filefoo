# FileFoo Overview

Not sure if `filefoo` will last as the name, but I see this project as a "kitchen sink" of file searching, moving, renaming, deleting, summarizing, etc. This project is totally re-inventing the wheel, meaning all of these things have already been done. In some cases maybe they will have been done better or faster. However, I would like an all-in-one command line tool for programmers that will allow them to do the aforementioned tasks using a `key=value` interface, as opposed to a one line `bash` / `regex` / `piped` / `awk` command. These types of commands are awesome, but typically not as robust as something that can be built over and over using `key=value` pairs to dictate what happens. 

In addition, the results of a command can be saved in a specified format (json,csv,etc.) to be put away for use later. I find that a lot of times I need to find a specific set of files that I don't need "moved" or "deleted" (for example), but I need them to process further. Having the ability to output results in some format will, in my opinion, be helpful.

## Goals

- Create a `pypi` worthy package using modern dev tools for students to learn project management
- Create a command line tool to do many things with files and directories

## Some Resources 

- To get started, here are some resources to look at:
  - https://packaging.python.org/tutorials/packaging-projects/
  - https://realpython.com/pyinstaller-python/
  - https://docs.python-guide.org/writing/structure/
  - https://choosealicense.com/licenses/gpl-3.0/

## So Far

### External Requirements

- So far this tool is using:
  - humanfriendly : for converting bytes to human readable sizes e.g. 1024 = 1K
  - columnar      : for nice tabular text output
  - clr           : color terminal output
  - whaaaaat      : uses prompt_toolkit and will be going away
  - prompt_toolkit: probably keep to help with terminal prompts

>Note: Look at [int_ex_choices.py](./int_ex_choices.py) and [int_ex_expand.py](./int_ex_expand.py) for examples on how a user may interact with filefoo after running a "find" command.


### Existing Functionality

```
|--------------|---------------------------------------------------------------------------------|
| Command      | Description                                                                     |
|================================================================================================|
| binary       | Convert byte file sizes into binary powers of 2.                                |
|--------------|---------------------------------------------------------------------------------|
| date         | Date to match files to (exact match) so be careful with times.                  |
|--------------|---------------------------------------------------------------------------------|
| file_types   | Allowed file types (e.g. =png,jpg,bmp ) (based on extension not file structure).|
|--------------|---------------------------------------------------------------------------------|
| min_date     | Min date for matched files (e.g. ="2019-02-22 13:30").                          |
|--------------|---------------------------------------------------------------------------------|
| max_date     | Max date for matched files.                                                     |
|--------------|---------------------------------------------------------------------------------|
| min_size     | Min allowed file size (e.g. =1000 or =1K or =4GB etc.).                         |
|--------------|---------------------------------------------------------------------------------|
| max_size     | Max allowed file size.                                                          |
|--------------|---------------------------------------------------------------------------------|
| out_filename | Name of file to save results of search.                                         |
|--------------|---------------------------------------------------------------------------------|
| path         | Start search here.                                                              |
|--------------|---------------------------------------------------------------------------------|
| print_summary| Print a tabular summary of files.                                               |
|--------------|---------------------------------------------------------------------------------|
| size         | Size file should be (with some delta because exact matches are not reliable).   |
|--------------|---------------------------------------------------------------------------------|
| size_delta   | Size delta for a size match (+/- some small value). Default = 1 percent of size.|
|--------------|---------------------------------------------------------------------------------|
| substr_match | String to partially match a filename.                                           |
|--------------|---------------------------------------------------------------------------------|
```

Examples:

- `filefoo fin path=~/ file_types=cpp,hpp,h,c`
- `filefoo fin path=~/ min_size=5MB file_types=osm`
- `filefoo fin file_types=jpg,png,bmp,tiff`


### Todo Ideas

- Find and rename files based on a naming pattern.
- Find and move files.
- Lowercase all files in 1 or more directories
- Change file naming type to `camelCase` or `snake_case` or `kebab-case` or ??
- Compare directory contents
- Find duplicate files
- Find leftover package folders (like node_modules) and others to eliminate
- Summarize or sShow what makes up a folder: 
  - most files of specific type
  - counts of each type
  - what takes up most space
  - temp files if any
  - pycache or similar
  - etc.
- Handle hidden files (ignore or not)
- Find top X largest files.
- Ignore backups (files or folders with `backup` in them?)
- When searching for files or folders, how do you figure out an approximate time remaining? 

Possible start to counting files / folders before a search to help with approx times.
```python
from os import listdir
from os.path import isfile, join
directory = '/home/myname/Maildir/new'
print(sum(1 for entry in listdir(directory) if isdir(join(directory,entry))))

# or for dirs

for entry in listdir(directory):
    if isdir(join(directory,entry)):
        print(entry)
```


### Problem

How do we structure and organize the existing code. We need to at the existing code base, come up with what other functionality we want to add (requirements), then decide on how to organize or structure our code base to allow for the addition of new functions without ruining the old code.

I tried to format the existing folder structure to be typical of a `pypi` package, but need help with `class` organization as well as `helper`/ `util` functions.

# srsly-cli

[![Python version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue.svg)](https://pypi.org/project/srsly-cli/)
[![PyPI version](https://badge.fury.io/py/srsly-cli.svg)](https://badge.fury.io/py/srsly-cli)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Minyus/srsly-cli/blob/main/LICENSE)

CLI to convert between JSON, JSONL, YAML, MessagePack

## Example

```bash
srsly --read-path sample.jsonl --write-path sample.yaml
```

In this example, `srsly.read_jsonl` and `srsly.write_yaml` are used.

## Supported data

The following data types supported.

- json
- jsonl
- yaml/yml
- gzip_json
- gzip_jsonl
- msgpack

If the extension in the read-path or write-path is not one of these, `--read-type` or `--write-type` needs to be set explicitly.

##

srsly --help

```
NAME
    srsly

SYNOPSIS
    srsly READ_PATH <flags>

POSITIONAL ARGUMENTS
    READ_PATH
        Type: str

FLAGS
    --write_path=WRITE_PATH
        Type: Optional[str]
        Default: None
    --read_type=READ_TYPE
        Type: Optional[str]
        Default: None
    --write_type=WRITE_TYPE
        Type: Optional[str]
        Default: None
    --read_skip=READ_SKIP
        Type: Optional[bool]
        Default: None
    --read_use_list=READ_USE_LIST
        Type: Optional[bool]
        Default: None
    --write_indent=WRITE_INDENT
        Type: Optional[int]
        Default: None
    --write_append=WRITE_APPEND
        Type: Optional[bool]
        Default: None
    --write_append_new_line=WRITE_APPEND_NEW_LINE
        Type: Optional[bool]
        Default: None
    --write_indent_mapping=WRITE_INDENT_MAPPING
        Type: Optional[int]
        Default: None
    --write_indent_sequence=WRITE_INDENT_SEQUENCE
        Type: Optional[int]
        Default: None
    --write_indent_offset=WRITE_INDENT_OFFSET
        Type: Optional[int]
        Default: None
    --write_sort_keys=WRITE_SORT_KEYS
        Type: Optional[bool]
        Default: None

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```

For details about the options, please refer `srsly.read_{DATA_TYPE}` and `srsly.write_{DATA_TYPE}` in:
https://github.com/explosion/srsly


## Dependencies

- https://github.com/explosion/srsly
- https://github.com/google/python-fire

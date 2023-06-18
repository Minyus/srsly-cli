# srsly-cli

CLI to convert between JSON, JSONL, YAML, MessagePack

## Example

```bash
srsly --read-path sample.jsonl --write-path sample.yaml
```

In this example, `srsly.read_jsonl` and `srsly.write_yaml` are used.

For details about the options, please refer:
https://github.com/explosion/srsly

## Supported data

The following data types supported.

- json
- jsonl
- yaml/yml
- gzip_json
- gzip_jsonl
- msgpack

If the extension in the path is not one of these, `--read-type` or `--write-type` needs to be set explicitly.

## dependencies

https://github.com/explosion/srsly
https://github.com/google/python-fire

# msgpack-tool

install via pip

```sh
pip install msgpack-tool
```

json to msgpack

```sh
curl -s https://api.github.com/repos/zweifisch/msgpack-tool | msgpack | hexdump -C | head
```

msgpack to json

```sh
curl -s https://api.github.com/repos/zweifisch/msgpack-tool | msgpack | msgpack
```

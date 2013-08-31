# msgpack-tool

install via pip

```sh
pip install msgpack-tool
```

json to msgpack

```sh
echo '{"compact": true, "schema": 0}' | msgpack | hexdump -C

00000000  82 a7 63 6f 6d 70 61 63  74 c3 a6 73 63 68 65 6d  |..compact..schem|
00000010  61 00                                             |a.|
00000012
```

msgpack to json

```sh
echo '{"compact": true, "schema": 0}' | msgpack | msgpack

{
  "compact": true, 
  "schema": 0
}
```

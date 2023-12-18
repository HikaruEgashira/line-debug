# Line Tool for Test

https://developers.line.biz/ja/docs/messaging-api/generate-json-web-token/

```sh
# generate public key, private key
poetry run python scripts/main key
```

LINEコンソールにアクセストークンを送りLINE_KIDを取得する

```sh
# generate access token
poetry run python scripts/main token
```

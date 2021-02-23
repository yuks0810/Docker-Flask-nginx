# Docker-Flask-nginx
参考：
[DockerでNGINX + NGINX Unit + MySQLの環境を構築](https://qiita.com/t_okkan/items/f4baba5ee29216522e08#)

## 使い方
git cloneを行った後

```bash
$ docker-compose down
$ docker-compose build --no-cache
$ docker-compose up
```

app_apのコンテナの起動後に、コンテナにアクセスしてNGINX Unitの設定ファイルを設定します。

```
$ docker exec -it app_ap bash
root@00000000000:/# curl -X PUT --data-binary @config.json --unix-socket /var/run/control.unit.sock http://localhost/config
{
    "success": "Reconfiguration done."
}
```

起動後
http://localhost:80
に接続

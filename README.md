# Installations
```
python -m pip install requests
```

```
pip install paho-mqtt
```

## Run subscriber
1st argument `topic`
```
python3 sub.py 'sensor/+/light'
```

## Run publisher
1st argument `topic`
2nd argument `message`
```
 python3 pub.py 'sensor/1/light' '5'
```

# CryptoCourceAutoposting
```bash
  
   _____                  _         _____                         
  / ____|                | |       / ____|                        
 | |     _ __ _   _ _ __ | |_ ___ | |     ___  _   _ _ __ ___ ___ 
 | |    | '__| | | | '_ \| __/ _ \| |    / _ \| | | | '__/ __/ _ \
 | |____| |  | |_| | |_) | || (_) | |___| (_) | |_| | | | (_|  __/
  \_____|_|   \__, | .__/ \__\___/ \_____\___/ \__,_|_|  \___\___|
               __/ | |                                            
              |___/|_|                   _   _                    
     /\        | |                      | | (_)                   
    /  \  _   _| |_ ___  _ __   ___  ___| |_ _ _ __   __ _        
   / /\ \| | | | __/ _ \| '_ \ / _ \/ __| __| | '_ \ / _` |       
  / ____ \ |_| | || (_) | |_) | (_) \__ \ |_| | | | | (_| |       
 /_/    \_\__,_|\__\___/| .__/ \___/|___/\__|_|_| |_|\__, |       
                        | |                           __/ |       
                        |_|                          |___/        
```
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![version](https://img.shields.io/badge/version-1.0-blue)]()

## About project
Данный репозиторий представляет собой исходники телеграм бота единственной функцией которого является автопостинг рыночного и p2p [buy/sell] курса криптовалюты 
в данном случае ETH в выбраный вами телеграм канал. 


## Pre deployment
Для деплоя данного проекта вам понадобится изменить некоторые данные в файле config.py

```bash
  TOKEN = "" #Токен вашего телеграм бота
  chanel_name = "" #Имя канала через @ например @CryptoAutoposting
  admin_id = 0 #ID вашего телеграм аккаунта
  delay = 120 #Задержка в секунадах (по стандарту 2 минуты)
```


## Deployment

Для деплоя самого бота после замены выше указаных данных на свои введите следующие команды

```bash
  pip -r requirements.txt
  python3 main.py
 ```
 

## API Reference Customisation


 Для получения сведений не об eth а о другой, нужной вам криптовалюте вам следует заменить API url на строках 14 и 18 

#### Пример измененного api на 14 строке для получения инфо о BTC 

```https
  https://yobit.net/api/3/ticker/btc_usd
```

| Parameter | Method     | Description                |
| :-------- | :------- | :------------------------- |
| `/btc_usd` | `ticker` | Сюда помещаем валютную пару |

#### Пример измененного api на 18 строке для получения инфо о BTC 

```https
  https://yobit.net/api/3/depth/btc_usd
```

| Parameter | Method     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `/btc_usd` | `depth` | Здесь тоже меняем валютную пару |


#### Contacts

[![Telegram](https://img.shields.io/badge/-telegram-red?style=for-the-badge&color=black&logo=telegram&logoColor=black)](https://t.me/classssik)


##### На этом все, спасибо за внимание!



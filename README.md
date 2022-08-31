# 🐼 Kuriboh 🪄

[![Uptime](https://status.pejedev.xyz/api/badge/7/uptime/720?label=30&labelSuffix=d)](https://status.pejedev.xyz)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

Microservice to calculate smallest postive interger not present on an array and retrieve statistics.

## Tech Stack

**Development:** Docker, Docker-compose, pytest, pylint.

**Server:** Python 3.8, Flask, Gunicorn, MongoDb.

**Deployment:** Dokku, Github Actions.

## Features

- Calculate smallest positive interger not present on an array.
- Get total of unique arrays validated through the API.
- Get Count of occurrence as a calculation result from a number.
- Get ratio between the total count of arrays calculated and result occurrence count from a number.
- Get server status.

## Demo

- <https://kuriboh.pejedev.xyz/api/smallest>
- <https://kuriboh.pejedev.xyz/api/stats>
- <https://kuriboh.pejedev.xyz/api/health>

## Run Locally

Clone the project

```bash
  git clone https://github.com/PejeDev/Kuriboh.git
```

Go to the project directory

```bash
  cd Kuriboh
```

Start the server

```bash
  docker-compose -D
```

## API Reference

### Calculate smallest postive interger not present on an array

```http
  POST /api/smallest
```

#### Body

```json
{
  “array”: [1, 3, 6, 4, 1, 2]
}

```

#### Response

```json
{
  “result”: 5
}

```

| Property | Type  | Description                                         |
| :------- | :---- | :-------------------------------------------------- |
| `result` | `int` | Smallest positive interger not present in an array. |

### Get number array calculation stats

```http
  GET /api/stats/${number}
```

| Parameter | Type  | Description                              |
| :-------- | :---- | :--------------------------------------- |
| `number`  | `int` | **Required**. Number to calculate stats. |

#### Response

```json
{
  “count”: 40,
  “total”: 100,
  “ratio”: 0.4
}

```

| Property | Type    | Description                                                                                   |
| :------- | :------ | :-------------------------------------------------------------------------------------------- |
| `count`  | `int`   | Count of the parameter number occurrence as a calculation result.                             |
| `total`  | `int`   | Number of unique arrays validated through the API and stored in a database.                   |
| `ratio`  | `float` | Ratio between the total count of arrays calculated and the number parameter occurrence count. |

### Get server status

```http
  GET /api/health
```

#### Response

```json
{
  "status": "ok"
}
```

## Authors

- [@PejeDev](https://github.com/PejeDev)

## License

[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

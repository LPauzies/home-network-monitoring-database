# Home network monitoring database

This repo setup the home network monitoring database.

## Initialization

Use `python database_initialization.py` to initialize database.

## Data Model

| Ping          |                                 |
|---------------|---------------------------------|
| EventTime     | Integer (Timestamp)             |
| IP            | Text (Matching XXX.XXX.XXX.XXX) |
| DomainName    | Text                            |
| IPDescription | Text                            |
| ResponseTime  | Real (in ms)                    |
| PacketLoss    | Integer (0 or 1 for a boolean)  |


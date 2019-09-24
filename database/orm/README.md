# ORM

An Object Relational Mapper for the War Postgres Database

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## Usage

To create a new instance and connect to the database set the following env vars and initialize the ORM class. 

#### Env Vars

* DATABASE
* USER
* PASSWORD
* HOST
* PORT

Doing so will automatically attempt to connect to the database.

## Methods

Currently there are the four basic functions to interact with the database:

* `get`
* `insert`
* `update`
* `delete`

If needed add more methods to better facilitate the needs of the database.

## Testing

To run the tests for the ORM package, run `make test`.
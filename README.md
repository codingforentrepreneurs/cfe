# CFE CLI
A command line tool for various CFE-related tutorials and services.

> Do you have ideas for features? Please tweet us [@joincfe](https://twitter.com/joincfe)

## Install

`pip install cfe`


## Services (`cfe services`)

```
cfe services
```
This will give you all of the available services.


### Linode (`cfe services linode`)


#### Instance Inventory  `cfe services linode inventory`

This is primarily made for usage with Ansible but it can be useful for many other things too.

``
export LINODE_ACCESS_TOKEN=your_linode_personal_access_token
``
> `LINODE_ACCESS_TOKEN` needs to be in environment variables

```
cfe services linode inventory --save-path "inventory.ini" --tags "webapps"
```
or

```
LINODE_ACCESS_TOKEN=your_linode_personal_access_token cfe services linode inventory
```

Options:

- `--all` Lists all Linode instance IP addresses and groups items by tags
- `--save-path` write a path to save a `inventory.ini` file
- `--tags` Use a comma separated list of tags you want to include (`--all` will override)

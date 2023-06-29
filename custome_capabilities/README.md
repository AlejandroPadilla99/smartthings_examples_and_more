Custome capabilities tutorial
--

Official documentation
- [Capabilites](https://developer.smartthings.com/docs/devices/capabilities/custom-capabilities)

Recommendade tools
- [SmartThing CLI](https://github.com/SmartThingsCommunity/smartthings-cli)


Topics
--
* Let's start
* Attributes
* Commands
* Attribute and Commands Constraints

Let's start
-
this is the basic structure of a capability
```json
{
    "name": "Example",
    "attributes": {
        ... 
    },
    "commands": {
        ...
    }
}
```

Attributes
--

This is the basic structure of atributes
```json

    "name_atribute":{
        "schema":{
            "properties":{
                "value":{
                    "type": "string",
                    ...
                }
            }
        },
        "additionalProperties": false
    },
    "required": [
            "value"
        ]

```
more information [here](https://developer.smartthings.com/docs/devices/capabilities/capabilities#attributes)


Commands
--
This is the basic structure of commands
```json
    "commands":{
        "command_name":{
            "arguments":[
                "name": "example",
                "optional": false,
                "schema": {
                    ...
                }
            ]
        }
    }
```
more information [here](https://developer.smartthings.com/docs/devices/capabilities/capabilities/#commands)

Attribute and Command Constraints
--
more information [here](https://developer.smartthings.com/docs/devices/capabilities/capabilities/#attribute-and-command-constraints)

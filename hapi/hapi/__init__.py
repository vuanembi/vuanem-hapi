from hapi.hapi import message_list

services = {
    i.name: i
    for i in [
        message_list.message_list,
    ]
}

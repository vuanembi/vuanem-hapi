from hapi.hapi import message_list, campaign_list, upload_list

services = {
    i.name: i
    for i in [
        message_list.message_list,
        campaign_list.campaign_list,
        upload_list.upload_list,
    ]
}

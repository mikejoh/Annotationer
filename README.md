# annotationer
A small script that helps you POST Events to the Graphite API. When i wrote this script i had to send a POST-request to two Graphite nodes because we had two servers behind a load balancer and the Event database wasn't mirrored between the nodes.

### Examples

```
$> annotationer.py -ip <IP1> <IP2> -w "Something happened" -t "tag1 tag2 tag3"
$> annotationer.py -ip <IP1> <IP2> -w "Something happened" -t "tag1 tag2 tag3" -e 1488326400
```

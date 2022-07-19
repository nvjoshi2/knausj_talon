# log this: 
#     insert("self.log.error()")
#     key("left")

kill chia:
    insert('chia stop all')
    key('enter')
    insert('ps -ef | grep chia_')
    key('enter')
    insert('kill ')

chia start node:
    chia start node

chia start wallet:
    chia start wallet


activate dart:
    insert('source ~/.bashrc')
    key('enter')

tab window:
    key('cmd-tab')

format document:
    key('cmd-s')
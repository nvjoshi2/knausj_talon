app: terminal
-
tag(): user.terminal
tag(): user.generic_unix_shell
activate vinv: 
    insert('. ./activate')
    key('enter')

deactivate vinv:
    insert('deactivate')
    key('enter')

find process:
    insert('ps -ef | grep ')

set chia environment:
    insert('export CHIA_ROOT=/Users/nvjoshi/.chia/testnet10')
    key('enter')
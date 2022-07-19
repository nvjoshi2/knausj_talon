wrap int:
    insert("(")
    key("left:2")
    insert("int")

insert to do:
    insert('# TODO')

add lock:
    insert('async with transaction_lock:')


add import:
    insert('from chia.util.db_factory import transaction_lock')
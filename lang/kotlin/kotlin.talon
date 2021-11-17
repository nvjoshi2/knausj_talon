mode: user.kotlin
mode: user.auto_lang
and code.language: kotlin
-

state of type <user.text>: 
    insert(": ")
    user.insert_formatted(text, "PUBLIC_CAMEL_CASE")
    insert(' ')

state dot <user.text>:
    insert(".")
    user.insert_formatted(text, "PRIVATE_CAMEL_CASE")


mode: user.kotlin
mode: user.auto_lang
and code.language: kotlin
-



^funky <user.text>$: user.code_public_function(text)
^empty funky <user.text>$: user.code_function_no_body(text)
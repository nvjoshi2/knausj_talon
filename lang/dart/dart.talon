mode: user.dart
mode: user.auto_lang
and code.language: dart
-

op question: ' ? '

op double question: ' ?? '
op colon: ' : '

op as: ' as '

read ref: 
    insert('ref.read()')
    key('left')

watch ref: 
    insert('ref.watch()')
    key('left')

named field <user.text>: user.constructor_call_named_field(text)

color theme: 'Theme.of(context).colorScheme'

text theme: 'Theme.of(context).textTheme'

new consumer widget <user.text>:
    user.define_widget(text, 'ConsumerWidget')

new hook consumer widget <user.text>:
    user.define_widget(text, 'HookConsumerWidget')

new widget <user.text>:
    user.define_widget(text, 'StatelessWidget')


construct field: 'required this'

list of <user.text>: user.code_define_list(text)
future of <user.text>: user.code_define_future(text)
variable <user.text> of type <user.text>$:user.type_variable(text_2, text_1)
type <user.text> $: user.format_and_insert_type(text)

^funky <user.text>$: user.code_public_function(text)
^typed funky <user.text> returning <user.text>$: user.code_typed_function(text_1, text_2)
# ^member funky <user.text>$: user.code_public_function(text)

make local: user.localize_text()

app localizations: 'AppLocalizations.of(context)!'

make from jason: '.fromJson(Map<String, dynamic> json)'
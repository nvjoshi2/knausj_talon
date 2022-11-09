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


construct field: 'required this.'

list of <user.text>: user.code_define_list(text)
future of <user.text>: user.code_define_future(text)
variable <user.text> of type <user.text>$:user.type_variable(text_2, text_1)
class variable <user.text> of type <user.text>$:user.initialize_type_variable(text_2, text_1)

type <user.text> $: user.format_and_insert_type(text)

^funky <user.text>$: user.code_public_function(text)
^typed funky <user.text> returning <user.text>$: user.code_typed_function(text_1, text_2)
# ^member funky <user.text>$: user.code_public_function(text)

make local: user.localize_text()

json object: 'Map<String, dynamic>'

app localizations: 'AppLocalizations.of(context)!'

make from jason: '.fromJson(Map<String, dynamic> json)'

make to json: 
    insert('Map<String, dynamic> toJson() => <String, dynamic>{')
    key('enter')

(wrap | rap) future: user.wrap_future()

state null return: 'return null;'

new provider: 'Provider((ref) {},);'
new family provider: 'Provider.family((ref, arg) {},);'

state try catch: 
    insert('try {}')
    key('left')
    key('enter')
    key('down')
    insert('on Exception catch(e) {}')
    key('left')
    key('enter')
    key('enter')
    key('up')

logging error: 
    insert('LoggingContext().error()')
    key('left')

logging info: 
    insert('LoggingContext().info()')
    key('left')

make to do: '// TODO(nvjoshi2): '

^lambda funky: user.code_lambda_function()
async lambda funky: 
    insert("() async {}")
    key("left")
    key("enter")


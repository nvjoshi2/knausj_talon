import re

from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.python
mode: user.auto_lang
and code.language: python
"""
ctx.lists["user.code_functions"] = {
    "enumerate": "enumerate",
    "integer": "int",
    "length": "len",
    "list": "list",
    "print": "print",
    "range": "range",
    "set": "set",
    "split": "split",
    "string": "str",
    "update": "update",
}

"""a set of fields used in python docstrings that will follow the
reStructuredText format"""
docstring_fields = {
    "class": ":class:",
    "function": ":func:",
    "parameter": ":param:",
    "raise": ":raise:",
    "returns": ":return:",
    "type": ":type:",
    "return type": ":rtype:",
    # these are sphinx-specific
    "see also": ".. seealso:: ",
    "notes": ".. notes:: ",
    "warning": ".. warning:: ",
    "todo": ".. todo:: ",
}

mod.list("python_docstring_fields", desc="python docstring fields")
ctx.lists["user.python_docstring_fields"] = docstring_fields

type_list = {
    "boolean": "bool",
    "integer": "int",
    "string": "str",
    "none": "None",
    "dick": "Dict",
    "float": "float",
    "any": "Any",
    "tuple": "Tuple",
    "union": "UnionAny",
    "iterable": "Iterable",
    "vector": "Vector",
    "bytes": "bytes",
    "sequence": "Sequence",
    "callable": "Callable",
    "list": "List",
    "no return": "NoReturn",
}

mod.list("python_type_list", desc="python types")
ctx.lists["user.python_type_list"] = type_list

exception_list = [
    "BaseException",
    "SystemExit",
    "KeyboardInterrupt",
    "GeneratorExit",
    "Exception",
    "StopIteration",
    "StopAsyncIteration",
    "ArithmeticError",
    "FloatingPointError",
    "OverflowError",
    "ZeroDivisionError",
    "AssertionError",
    "AttributeError",
    "BufferError",
    "EOFError",
    "ImportError",
    "ModuleNotFoundError",
    "LookupError",
    "IndexError",
    "KeyError",
    "MemoryError",
    "NameError",
    "UnboundLocalError",
    "OSError",
    "BlockingIOError",
    "ChildProcessError",
    "ConnectionError",
    "BrokenPipeError",
    "ConnectionAbortedError",
    "ConnectionRefusedError",
    "ConnectionResetError",
    "FileExistsError",
    "FileNotFoundError",
    "InterruptedError",
    "IsADirectoryError",
    "NotADirectoryError",
    "PermissionError",
    "ProcessLookupError",
    "TimeoutError",
    "ReferenceError",
    "RuntimeError",
    "NotImplementedError",
    "RecursionError",
    "SyntaxError",
    "IndentationError",
    "TabError",
    "SystemError",
    "TypeError",
    "ValueError",
    "UnicodeError",
    "UnicodeDecodeError",
    "UnicodeEncodeError",
    "UnicodeTranslateError",
    "Warning",
    "DeprecationWarning",
    "PendingDeprecationWarning",
    "RuntimeWarning",
    "SyntaxWarning",
    "UserWarning",
    "FutureWarning",
    "ImportWarning",
    "UnicodeWarning",
    "BytesWarning",
    "ResourceWarning",
]
mod.list("python_exception", desc="python exceptions")
ctx.lists["user.python_exception"] = {
    " ".join(re.findall("[A-Z][^A-Z]*", exception)).lower(): exception
    for exception in exception_list
}


@ctx.action_class("user")
class UserActions:
    def code_operator_indirection():           actions.auto_insert('')
    def code_operator_address_of():            actions.auto_insert('')
    def code_operator_structure_dereference(): actions.auto_insert('')
    def code_operator_lambda():                actions.auto_insert('')
    def code_operator_subscript():
        actions.insert('[]')
        actions.key('left')
    def code_operator_assignment():                      actions.auto_insert(' = ')
    def code_operator_subtraction():                     actions.auto_insert(' - ')
    def code_operator_subtraction_assignment():          actions.auto_insert(' -= ')
    def code_operator_addition():                        actions.auto_insert(' + ')
    def code_operator_addition_assignment():             actions.auto_insert(' += ')
    def code_operator_multiplication():                  actions.auto_insert(' * ')
    def code_operator_multiplication_assignment():       actions.auto_insert(' *= ')
    def code_operator_exponent():                        actions.auto_insert(' ** ')
    def code_operator_division():                        actions.auto_insert(' / ')
    def code_operator_division_assignment():             actions.auto_insert(' /= ')
    def code_operator_modulo():                          actions.auto_insert(' % ')
    def code_operator_modulo_assignment():               actions.auto_insert(' %= ')
    def code_operator_equal():                           actions.auto_insert(' == ')
    def code_operator_not_equal():                       actions.auto_insert(' != ')
    def code_operator_greater_than():                    actions.auto_insert(' > ')
    def code_operator_greater_than_or_equal_to():        actions.auto_insert(' >= ')
    def code_operator_less_than():                       actions.auto_insert(' < ')
    def code_operator_less_than_or_equal_to():           actions.auto_insert(' <= ')
    def code_operator_and():                             actions.auto_insert(' and ')
    def code_operator_or():                              actions.auto_insert(' or ')
    def code_operator_bitwise_and():                     actions.auto_insert(' & ')
    def code_operator_bitwise_and_assignment():          actions.auto_insert(' &= ')
    def code_operator_bitwise_or():                      actions.auto_insert(' | ')
    def code_operator_bitwise_or_assignment():           actions.auto_insert(' |= ')
    def code_operator_bitwise_exclusive_or():            actions.auto_insert(' ^ ')
    def code_operator_bitwise_exclusive_or_assignment(): actions.auto_insert(' ^= ')
    def code_operator_bitwise_left_shift():              actions.auto_insert(' << ')
    def code_operator_bitwise_left_shift_assignment():   actions.auto_insert(' <<= ')
    def code_operator_bitwise_right_shift():             actions.auto_insert(' >> ')
    def code_operator_bitwise_right_shift_assignment():  actions.auto_insert(' >>= ')
    def code_self():                                     actions.auto_insert('self')
    def code_null():                                     actions.auto_insert('None')
    def code_is_null():                                  actions.auto_insert(' is None')
    def code_is_not_null():                              actions.auto_insert(' is not None')
    def code_state_if():
        actions.insert('if :')
        actions.key('left')
    def code_state_else_if():
        actions.insert('elif :')
        actions.key('left')
    def code_state_else():
        actions.insert('else:')
        actions.key('enter')
    def code_state_switch():
        actions.insert('switch ()')
        actions.edit.left()
    def code_state_case():
        actions.insert('case \nbreak;')
        actions.edit.up()
    def code_state_for(): actions.auto_insert('for ')
    def code_state_for_each():
        actions.insert('for in ')
        actions.key('left')
        actions.edit.word_left()
        actions.key('space')
        actions.edit.left()
    def code_state_while():
        actions.insert('while :')
        actions.edit.left()
    def code_type_class(): actions.auto_insert('class ')
    def code_import():     actions.auto_insert('import ')
    def code_from_import():
        actions.insert('from import ')
        actions.key('left')
        actions.edit.word_left()
        actions.key('space')
        actions.edit.left()
    def code_comment(): actions.auto_insert('# ')
    def code_state_return():
        actions.insert('return ')
    def code_true():            actions.auto_insert('True')
    def code_false():           actions.auto_insert('False')
    def code_document_string(): actions.user.insert_cursor('"""[|]"""')
    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"
        actions.user.paste(text)
        actions.edit.left()
    

    def code_refactor_create_task(selection: str):
        start = 'asyncio.create_task('
        end = ')'
        function_call = selection[selection.find(start)+len(start):selection.rfind(end)]

        actions.user.paste(f"await {function_call}")


    def code_refactor_index(type: str, selection: str):
        selection = selection.lower()
        if type == 'create':
            #get database
            start = '('
            end = ', \"'
            database = selection[selection.find(start)+len(start):selection.rfind(end)]

            #get query
            start = '\"'
            end = '\"'
            query = selection[selection.find(start)+len(start):selection.rfind(end)]

            #get index_name
            start = 'create index if not exists '
            end = ' on '
            index_name = query[query.find(start)+len(start):query.rfind(end)]

            #get table_name
            start = ' on '
            end = '('
            table_name = query[query.find(start)+len(start):query.rfind(end)]

            #get index_columns
            start = '('
            end = ')'
            index_columns_string = query[query.find(start)+len(start):query.rfind(end)]
            index_columns = map(lambda s: f"'{s.strip()}'", index_columns_string.split(','))

            #get condition
            condition = query.split('where')[-1]

            to_insert = f"({database}, '{index_name}', '{table_name}', [{', '.join(index_columns)}]"
            if len(condition) < len(query):
                to_insert = to_insert + f", '{condition.strip()}')"
            else:
                to_insert = to_insert + ")"
            
            actions.user.paste(to_insert)
        
        # elif type == 'drop':

    def code_refactor_query(selection: str):
        
        lines = list(map(lambda line: line.strip(), selection.split("\n")))

        to_insert = ''
        if len(lines) > 1:
            to_insert += "{\n"
            for i in range(1, len(lines) - 1):
                line = lines[i].strip() # remove leading/trailing white spaces
                if line:
                    print(line)
                    to_insert += ('  "": ' + line + '\n')
            to_insert+= "}"
        
        else:
            line = lines[0].strip()
            line = line[1:-1]
            fields = line.split(',')
            fields = list(filter(lambda field: field != '' and field != ' ', fields))
            to_insert += '{'
            for i in range(len(fields)):
                field = fields[i]
                if field:
                    if i == len(fields) - 1:
                        to_insert += ('"": ' + field) 
                    else:
                        to_insert += ('"": ' + field + ', ') 
            to_insert += '}'
        
        actions.user.paste(to_insert)


    def code_default_function(text: str):
        actions.user.code_public_function(text)

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "def _{}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_public_function(text: str):
        result = "def {}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()


@mod.action_class
class module_actions:
    # TODO this could go somewhere else
    def insert_cursor(text: str):
        """Insert a string. Leave the cursor wherever [|] is in the text"""
        if "[|]" in text:
            end_pos = text.find("[|]")
            s = text.replace("[|]", "")
            actions.insert(s)
            actions.key(f"left:{len(s) - end_pos}")
        else:
            actions.insert(text)

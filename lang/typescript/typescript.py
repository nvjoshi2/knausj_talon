from talon import Module, Context, actions, ui, imgui, settings

ctx = Context()
ctx.matches = r"""
mode: user.typescript
mode: user.auto_lang 
and code.language: typescript
"""
# tbd
ctx.lists["user.code_functions"] = {
    "integer": "int.TryParse",
    "print": "console.log",
    "string": ".ToString",
}
defaultType = "const"
ctx.lists["user.variable_types"] = {
    "mutable": "let",
    "immutable": defaultType,
}


@ctx.action_class("user")
class UserActions:
    def format_and_insert_type(type: str):
        if type in ['bool','boolean', 'number', 'undefined', 'string', ]:
            if(type == 'bool'):
                actions.insert('boolean')
            else:
                actions.insert(type)
        else:
            actions.user.insert_formatted(type, "PUBLIC_CAMEL_CASE")
            
    def type_variable(type: str, variable_name: str):
        actions.user.insert_formatted(variable_name, "PRIVATE_CAMEL_CASE")
        actions.insert(": ")
        UserActions.format_and_insert_type(type)

    def code_give_type(type1: str):
        actions.insert(": ")
        UserActions.format_and_insert_type(type1)
    
    def code_define_list(innerType: str):
        actions.insert('Array<')
        UserActions.format_and_insert_type(innerType)       
        actions.insert('>')

    def constructor_call_named_field(field: str):
        actions.user.insert_formatted(field, "PRIVATE_CAMEL_CASE")
        actions.insert(": ")



    def code_initialize_variable(variableType: str, variableName: str):
        if (variableType == "no_spoken_type"):
            actions.insert(defaultType)
        else:
            actions.insert(variableType)
        
        actions.insert(" ")
        actions.user.insert_formatted(variableName, "PRIVATE_CAMEL_CASE")
        
    def code_is_not_null():
        actions.auto_insert(" !== null")

    def code_is_null():
        actions.auto_insert(" === null")

    def code_type_dictionary():
        actions.insert("{}")
        actions.key("left")

    def code_state_if():
        actions.insert("if ()")
        actions.key("left")

    def code_state_else_if():
        actions.insert(" else if ()")
        actions.key("left")

    def code_state_else():
        actions.insert(" else {}")
        actions.key("left enter")

    def code_block():
        actions.insert("{}")
        actions.key("left enter")

    def code_self():
        actions.auto_insert("this")

    def code_state_while():
        actions.insert("while ()")
        actions.key("left")

    def code_state_do():
        actions.insert("do ")

    def code_state_return():
        actions.insert("return ")

    def code_state_for():
        actions.insert("for ()")
        actions.key("left")

    def code_state_switch():
        actions.insert("switch ()")
        actions.key("left")

    def code_state_case():
        actions.auto_insert("case :")

    def code_state_go_to():
        actions.auto_insert("")

    def code_import():
        actions.auto_insert("import ")

    def code_from_import():
        actions.insert(' from  ""')
        actions.key("left")

    def code_type_class():
        actions.auto_insert("class ")

    def code_include():
        actions.auto_insert("")

    def code_include_system():
        actions.auto_insert("")

    def code_include_local():
        actions.auto_insert("")

    def code_type_definition():
        actions.auto_insert("")

    def code_typedef_struct():
        actions.auto_insert("")

    def code_state_for_each():
        actions.insert(".forEach()")
        actions.key("left")

    def code_break():
        actions.auto_insert("break;")

    def code_next():
        actions.auto_insert("continue;")

    def code_true():
        actions.auto_insert("true")

    def code_false():
        actions.auto_insert("false")

    def code_null():
        actions.auto_insert("null")

    def code_operator_indirection():
        actions.auto_insert("")

    def code_operator_address_of():
        actions.auto_insert("")

    def code_operator_structure_dereference():
        actions.auto_insert("")

    def code_operator_lambda():
        actions.auto_insert(" => ")

    def code_operator_subscript():
        actions.insert("[]")
        actions.key("left")

    def code_operator_assignment():
        actions.auto_insert(" = ")

    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_subtraction_assignment():
        actions.auto_insert(" -= ")

    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_addition_assignment():
        actions.auto_insert(" += ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    def code_operator_multiplication_assignment():
        actions.auto_insert(" *= ")

    def code_operator_exponent():
        actions.auto_insert(" ** ")

    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_division_assignment():
        actions.auto_insert(" /= ")

    def code_operator_modulo():
        actions.auto_insert(" % ")

    def code_operator_modulo_assignment():
        actions.auto_insert(" %= ")

    def code_operator_equal():
        actions.auto_insert(" == ")

    def code_operator_not_equal():
        actions.auto_insert(" != ")

    def code_operator_greater_than():
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(" >= ")

    def code_operator_less_than():
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(" <= ")

    def code_operator_and():
        actions.auto_insert(" && ")

    def code_operator_or():
        actions.auto_insert(" || ")

    def code_operator_bitwise_and():
        actions.auto_insert(" & ")

    def code_operator_bitwise_and_assignment():
        actions.auto_insert(" &= ")

    def code_operator_bitwise_or():
        actions.auto_insert(" | ")

    def code_operator_bitwise_or_assignment():
        actions.auto_insert(" |= ")

    def code_operator_bitwise_exclusive_or():
        actions.auto_insert(" ^ ")

    def code_operator_bitwise_exclusive_or_assignment():
        actions.auto_insert(" ^= ")

    def code_operator_bitwise_left_shift():
        actions.auto_insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.auto_insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.auto_insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.auto_insert(" >>= ")

    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "private function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    # def code_private_static_function(text: str):
    #     """Inserts private static function"""
    #     result = "private static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_private_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    def code_protected_function(text: str):
        result = "protected function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    # def code_protected_static_function(text: str):
    #     result = "protected static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_protected_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    def code_public_function(text: str):
        result = "public function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_call_function(text: str):
        actions.user.insert_formatted(text, "PRIVATE_CAMEL_CASE")
        actions.insert('()')
        actions.key('left')


    # def code_public_static_function(text: str):
    #     result = "public static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_public_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)


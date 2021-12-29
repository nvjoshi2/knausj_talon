from talon import Context, actions, settings

ctx = Context()
ctx.matches = r"""
mode: user.kotlin
mode: user.auto_lang
and code.language: kotlin
"""
ctx.tags = ["user.code_operators", "user.code_generic"]

defaultType = "val"
ctx.lists["user.variable_types"] = {
    "mutable": "var",
    "immutable": defaultType,
}

ctx.lists["user.code_functions"] = {
    "print": "println",
}

@ctx.action_class("user")
class UserActions:
    def code_initialize_variable(variableType: str, variableName: str):
        if (variableType == "no_spoken_type"):
            actions.insert(defaultType)
        else:
            actions.insert(variableType)
        
        actions.insert(" ")
        actions.user.insert_formatted(variableName, "PRIVATE_CAMEL_CASE")

    def code_initialized_database_transaction():
        actions.insert("dbContext.transaction { trx -> }")
        actions.key("left")
        actions.key("enter")

    def code_give_type(type1: str):
        actions.insert(": ")
        if (type1 == "uuid"):
            actions.user.insert_formatted(type1, "SNAKE_CASE_CAP")
        else:
            actions.user.insert_formatted(type1, "PUBLIC_CAMEL_CASE")
    
    def code_operator_indirection():
        actions.skip()

    def code_operator_address_of():
        actions.skip()

    def code_operator_lambda():
        actions.auto_insert(" -> ")

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
        actions.auto_insert(" ^ ")

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

    def code_operator_bitwise_or():
        actions.auto_insert(" | ")

    def code_operator_bitwise_exclusive_or():
        actions.auto_insert(" ^ ")

    def code_operator_bitwise_left_shift():
        actions.auto_insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.auto_insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.auto_insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.auto_insert(" >>= ")

    def code_self():
        actions.auto_insert("this")

    def code_null():
        actions.auto_insert("null")

    def code_is_null():
        actions.auto_insert(" == null")

    def code_is_not_null():
        actions.auto_insert(" != null")

    def code_state_if():
        actions.insert("if () ")
        actions.key("left")
        actions.key("left")

    def code_state_else_if():
        actions.insert("else if () ")
        actions.key("left")
        actions.key("left")

    def code_state_else():
        actions.insert("else ")
        actions.key("enter")

    def code_state_switch():
        actions.insert("switch () ")
        actions.key("left")
        actions.edit.left()

    def code_state_case():
        actions.insert("case \nbreak;")
        actions.edit.up()

    def code_state_for():
        actions.insert("for () ")
        actions.key("left")
        actions.key("left")

    def code_state_while():
        actions.insert("while () ")
        actions.edit.left()
        actions.edit.left()

    def code_type_class():
        actions.auto_insert("class ")

    def code_default_function(text: str):
        actions.user.code_public_function(text)

    def code_private_function(text: str):
        actions.insert("private")

    def code_protected_function(text: str):
        actions.user.code_private_function()

    def code_public_function(text: str):
        actions.insert("fun ")
        actions.user.insert_formatted(text, "PRIVATE_CAMEL_CASE")
        actions.insert("() ")
        actions.insert("{}")
        actions.edit.left()
        actions.key("enter")
        actions.edit.up()
        actions.edit.line_end()
        actions.key("left:3")

    def code_function_no_body(text: str):
        actions.insert("fun ")
        actions.user.insert_formatted(text, "PRIVATE_CAMEL_CASE")
        actions.insert("() = ")
        actions.key("left:4")

    def code_state_return():
        actions.insert("return ")

    def code_insert_function(text: str, selection: str):
        actions.insert(text)
        actions.insert('()')
        actions.key("left")




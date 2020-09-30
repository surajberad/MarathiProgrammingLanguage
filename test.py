number = '०१२३४५६७८९'


def eng_to_mar(num):
    eng_num = str(num)
    mar_num = ''

    i = 0
    while i < len(eng_num):
        char = int(eng_num[i])
        mar_num += number[char]
        i += 1

    print(mar_num)


eng_to_mar(25245665)


#######################################
# INTERPRETER
#######################################

class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

#######################################


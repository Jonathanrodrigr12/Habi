class operatorUtils():

    def getValue(operation,value):
        dictOperator = {
            "=": f" = '{value}' ",
            "==": f" = '{value}' ",
            "equals": f" = '{value}' ",
            "eq": f" = '{value}' ",
            "!=":  f" != '{value}' ",
            "<>":  f" != '{value}' ",
            "ne":  f" != '{value}' ",
            "notequals": f" != '{value}' ",
            "startswith": f" like %'{value}' ",
            "endswith": f" like '{value}'% ",
            "mayor": f" > '{value}' ",
            ">": f" > '{value}' ",
            "mayorIgual": f" >= '{value}' ",
            ">=": f" >= '{value}' ",
            "menor": f" < '{value}' ",
            "<": f" < '{value}' ",
            "menorIgual": f" <= '{value}' ",
            "<=": f" < '{value}' "
        }
        return dictOperator[operation]

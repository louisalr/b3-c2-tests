import math

class Calculator:
    def calculate(expression):
        # Supprimer les espaces en trop de l'expression
        expression = expression.replace(" ", "")

        # Convertir l'expression en une liste de tokens (nombres et opérateurs)
        tokens = []
        current_token = ""

        for char in expression:
            if char.isdigit() or char == ".":
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)

        if current_token:
            tokens.append(current_token)
        
        # Évaluer l'expression 
        output_queue = []
        operator_stack = []
        operator_precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 2, "√": 4}

        for token in tokens:
            if token.isdigit() or "." in token:
                output_queue.append(float(token))
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack[-1] != "(":
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()
            elif token in operator_precedence:
                while operator_stack and operator_stack[-1] != "(" and operator_precedence[token] <= operator_precedence[operator_stack[-1]]:
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output_queue.append(operator_stack.pop())

        # Calculer le résultat de l'expression à partir de la file de sortie
        operand_stack = []
        for token in output_queue:
            if isinstance(token, float):
                operand_stack.append(token)
            elif token == "%":
                operand1 = operand_stack.pop()
                operand2 = operand_stack.pop()
                result = operand1 * operand2 * 0.01
                operand_stack.append(result)
            elif token == "√":
                operand1 = operand_stack.pop()
                result = math.sqrt(operand1)
                operand_stack.append(result)
            elif token in operator_precedence:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    if operand2 == 0:
                        return "Division par zéro impossible"
                    result = operand1 / operand2
                elif token == "^":
                    result = operand1 ** operand2

                operand_stack.append(result)

        # On retourne & print le résultat
        print("")
        print(str(result))
        print("")
        
        return operand_stack[0]
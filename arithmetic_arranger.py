def arithmetic_arranger(problems, operation=False):

    # Too many problems passed
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize each output row string - finally, each row will be joined depend on the value of second argument.
    rows = ['  ', '', '--', '']

    for problem in problems:
        (term_1, op, term_2) = problem.split(' ')

        # Operator check
        if (op != '+' and op != '-'):
            return "Error: Operator must be '+' or '-'."

        # Problem's terms check
        if not str.isdigit(term_1) or not str.isdigit(term_2):
            return "Error: Numbers must only contain digits."

        # Each term's length check
        if len(term_1) > 4 or len(term_2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # For first, second and third row, three situations can be considered about term_1 and term_2
        if len(term_1) == len(term_2):
            rows[0] += term_1
            rows[1] += op + ' ' + term_2

            rows[2] += '-' * len(term_1)

        elif len(term_1) > len(term_2):
            rows[0] += term_1
            rows[1] += op + ' '

            # Add indent for second row
            rows[1] += ' ' * (len(term_1) - len(term_2))

            rows[1] += term_2

            rows[2] += '-' * len(term_1)

        else:
            # Add indent for first row
            rows[0] += ' ' * (len(term_2) - len(term_1))

            rows[0] += term_1
            rows[1] += op + ' ' + term_2

            rows[2] += '-' * len(term_2)

        if problem == problems[-1]:
            if operation:
                rows[2] += '\n'
            else:
                rows[2] += ''
        else:
            # Add four spaces between each probrem and then initialize for next problem
            rows[0] += '      '
            rows[1] += '    '
            rows[2] += '    --'

        # Fourth row will be required depend on the value of second argument
        if operation:
            if op == '+':
                sum = str(int(term_1) + int(term_2))

                if (len(sum) > len(term_1)
                        and len(str(int(term_1) + int(term_2))) > len(term_2)):
                    rows[3] += ' ' + sum
                else:
                    rows[3] += '  ' + sum

            else:
                diff = str(int(term_1) - int(term_2))

                if int(term_1) - int(term_2) >= 0:
                    rows[3] += '  '

                    for _ in range(len(term_1) - len(diff)):
                        rows[3] += ' '

                else:
                    rows[3] += ' '

                    # The answer 'diff' contains minus symbol
                    rows[3] += ' ' * (len(term_2) - len(diff) + 1)

                rows[3] += diff

            if problem != problems[-1]:
                rows[3] += '    '

    rows[0] += '\n'
    rows[1] += '\n'

    if operation:
        arranged_problems = ''.join(rows)
    else:
        arranged_problems = ''.join(rows[:-1])

    return arranged_problems

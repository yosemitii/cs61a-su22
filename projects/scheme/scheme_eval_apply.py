import sys

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    # operators go into this condition
    # print("DEBUG: evaluating: ", expr)
    if scheme_symbolp(expr):
        # print("DEBUG: returning expr symbol: ", env.lookup(expr))
        return env.lookup(expr)
    # operands and nil go into this condition
    elif self_evaluating(expr):
        # print("DEBUG: returning expr", type(expr))
        # print("DEBUG: returning expr symbol: ", expr)

        return expr

    # All non-atomic expressions are lists (combinations)
    # print("DEBUG: expr:", expr)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    # print("DEBUG: first: ", type(first), " rest: ", rest)
    # print("DEBUG: ", rest is nil)
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3'
        operator = scheme_eval(first, env)
        validate_procedure(operator)
        operands = rest.map(lambda x: scheme_eval(x, env))
        return scheme_apply(operator, operands, env)
            # return scheme_eval(operator.py_func(rest, env), env)
        # END PROBLEM 3


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
       assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        lst = []
        pointer = args
        while pointer is not nil:
            lst = lst + [pointer.first]
            pointer = pointer.rest
        if procedure.need_env:
            lst = lst + [env]
        # END PROBLEM 2
        try:
            # BEGIN PROBLEM 2
            "*** YOUR CODE HERE ***"
            return procedure.py_func(*lst)
            # END PROBLEM 2
        except TypeError as err:
            raise SchemeError('incorrect number of arguments: {0}'.format(procedure))
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        # print("DEBUG: ", env, "formals", procedure.formals)
        # print("DEBUG: ", env, "args: ", args)
        #######################################
        # remember this, this is dynamic scope
        # child_frame = env.make_child_frame(procedure.formals, args)
        child_frame = procedure.env.make_child_frame(procedure.formals, args)

        # print("DEBUG: body: ", procedure.body, "child frame: ", child_frame)
        # print("DEBUG: parent frame:", child_frame.parent)
        # print("DEBUG: ===========================")
        return eval_all(procedure.body, child_frame)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        child_frame = env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, child_frame)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    print("DEBUG: evalutate", expressions)
    if expressions is nil:
        return None
    # Loop
    while expressions.rest != nil:
        scheme_eval(expressions.first, env)
        expressions = expressions.rest
    return scheme_eval(expressions.first, env, True)  # replace this with lines of your own code
    # Recursion
    # elif expressions.rest is nil:
    #     return scheme_eval(expressions.first, env, True)
    # else:
    #     scheme_eval(expressions.first, env)
    #     return eval_all(expressions.rest, env)
    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val


def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        result = Unevaluated(expr, env)
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        unoptimized_scheme_eval(result.expr, result.env)
        while isinstance(result, Unevaluated):
            result = unoptimized_scheme_eval(result.expr, result.env)
        return result
        # END PROBLEM EC
    return optimized_eval


################################################################
# Uncomment the following line to apply tail call optimization #
################################################################
scheme_eval = optimize_tail_calls(scheme_eval)


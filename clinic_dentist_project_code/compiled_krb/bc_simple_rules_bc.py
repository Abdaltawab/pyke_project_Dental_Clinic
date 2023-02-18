# bc_simple_rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def wear_rain_protection(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.wear_rain_protection: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_raincoat(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'rain_protection', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_bring_raincoat: got unexpected plan from when clause 1"
            with engine.prove('facts', 'windy', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_bring_raincoat: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_umbrella(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'rain_protection', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_bring_umbrella: got unexpected plan from when clause 1"
            with engine.prove('facts', 'windy', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_bring_umbrella: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_nothing(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_bring_nothing: got unexpected plan from when clause 1"
            with engine.prove('facts', 'windy', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_bring_nothing: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules')
  
  bc_rule.bc_rule('wear_rain_protection', This_rule_base, 'rain_protection',
                  wear_rain_protection, None,
                  (pattern.pattern_literal(True),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_bring_raincoat', This_rule_base, 'what_to_bring',
                  what_to_bring_raincoat, None,
                  (pattern.pattern_literal('raincoat'),),
                  (),
                  (contexts.variable('protection'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_bring_umbrella', This_rule_base, 'what_to_bring',
                  what_to_bring_umbrella, None,
                  (pattern.pattern_literal('umbrella'),),
                  (),
                  (contexts.variable('protection'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_nothing', This_rule_base, 'what_to_bring',
                  what_to_bring_nothing, None,
                  (pattern.pattern_literal('nothing'),),
                  (),
                  (pattern.pattern_literal(False),))


Krb_filename = '..\\bc_simple_rules.krb'
Krb_lineno_map = (
    ((14, 18), (14, 14)),
    ((20, 25), (16, 16)),
    ((38, 42), (19, 19)),
    ((44, 49), (21, 21)),
    ((50, 55), (22, 22)),
    ((68, 72), (25, 25)),
    ((74, 79), (27, 27)),
    ((80, 85), (28, 28)),
    ((98, 102), (31, 31)),
    ((104, 109), (33, 33)),
    ((110, 115), (34, 34)),
)

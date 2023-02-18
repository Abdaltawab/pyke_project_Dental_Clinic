# bc_simple_rules_questions_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def num_case0(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_yellow_spot', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case0: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case1(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_white_spot', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case1: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case2(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_yellow_stain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case2: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_gray_black_color_stain', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case2: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_discolor', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case2: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case3(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_yellow_color_stain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case3: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_gray_black_color_stain', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case3: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_discolor', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case3: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case4(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_yellow_color_stain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case4: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_gray_black_color_stain', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case4: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_discolor', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case4: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case5(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_yellow_color_stain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case5: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_gray_black_color_stain', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case5: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_discolor', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case5: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case6(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_yellow_color_stain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case6: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_gray_black_color_stain', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case6: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_discolor', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case6: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case7(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_yellow_color_stain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case7: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_gray_black_stain', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case7: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_discolor', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case7: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case8(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_yellow_color_stain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case8: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_gray_black_stain', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case8: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_discolor', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case8: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case9(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_yellow_color_stain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case9: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_gray_black_stain', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case9: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_discolor', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case9: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection1(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection2(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection2: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection3(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection3: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,4):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection4(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection4: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (5,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_you_have_Gingivitis_from_another_reson(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_red_and_swollen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_you_have_Gingivitis_from_another_reson: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_you_have_Gingivitis_from_one_reson(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_bleed', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_you_have_Gingivitis_from_one_reson: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_you_havenot_Gingivitis(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_red_and_swollen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_you_havenot_Gingivitis: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_bleed', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.what_you_havenot_Gingivitis: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_you_have_Gingivitis(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_red_and_swollen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_you_have_Gingivitis: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_bleed', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.what_you_have_Gingivitis: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_you_have_periodontitis(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_bleed', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_you_have_periodontitis: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pull_away_from_the_teeth', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.what_you_have_periodontitis: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_you_have_not_periodontitis(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_bleed', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_you_have_not_periodontitis: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pull_away_from_the_teeth', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.what_you_have_not_periodontitis: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case00(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_white_spot', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case00: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case01(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_white_spot', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case01: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case02(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_cavitation', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case02: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_black_color_stain', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case02: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_grayish_color', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case02: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case03(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_cavitation', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case03: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_black_color_stain', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case03: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_grayish_color', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case03: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case04(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_cavitation', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case04: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_black_color_stain', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case04: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_grayish_color', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case04: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case05(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_cavitation', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case05: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_black_color_stain', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case05: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_grayish_color', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case05: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case06(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_cavitation', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case06: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_black_color_stain', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case06: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_grayish_color', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case06: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case07(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_cavitation', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case07: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_black_color_stain', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case07: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_grayish_color', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case07: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case08(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_cavitation', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case08: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_black_color_stain', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case08: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_grayish_color', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case08: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case09(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_cavitation', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case09: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_black_color_stain', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case09: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_grayish_color', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case09: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection01(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_Things', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection01: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection02(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_Things', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection02: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection03(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_Things', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection03: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,4):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection11(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_Causes_disease', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection11: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,2):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection12(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_Causes_disease', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection12: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection13(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_Causes_disease', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection13: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case11(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_redness_the_gums', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case11: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case12(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_redness_the_gums', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case12: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_side_effect', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case12: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_poor_dental', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case12: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case13(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_redness_the_gums', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case13: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_side_effect', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case13: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_poor_dental', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case13: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case14(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_redness_the_gums', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case14: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_side_effect', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case14: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_poor_dental', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case14: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case15(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_redness_the_gums', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case15: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_side_effect', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case15: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_poor_dental', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case15: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case20(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_pain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case20: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case21(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_white_spot', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case21: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case22(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_pain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case22: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_fever', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case22: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_bacterial_infections', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case22: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case23(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_pain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case23: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_fever', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case23: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_bacterial_infections', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case23: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case24(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_pain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case24: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_fever', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case24: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_bacterial_infections', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case24: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case25(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_pain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case25: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_fever', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case25: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_bacterial_infections', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case25: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case26(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_pain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case26: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_fever', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case26: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_bacterial_infections', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case26: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case27(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_pain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case27: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_fever', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case27: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_bacterial_infections', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case27: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case28(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_pain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case28: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_fever', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case28: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_bacterial_infections', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case28: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def num_case29(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'is_pain', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.num_case29: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_fever', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.num_case29: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_bacterial_infections', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.num_case29: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection21(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection21: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection22(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection22: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection23(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection23: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,4):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_selection24(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'any_disasters2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_selection24: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (5,6):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules_questions')
  
  bc_rule.bc_rule('num_case0', This_rule_base, 'what_to_should',
                  num_case0, None,
                  (pattern.pattern_literal('Keep_clean_teeth_BY_Toothbrush'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case1', This_rule_base, 'what_to_should',
                  num_case1, None,
                  (pattern.pattern_literal('this_is_normal_however_Keep_clean_teeth_BY_Toothbrush'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case2', This_rule_base, 'what_to_should',
                  num_case2, None,
                  (pattern.pattern_literal('Thank_goodness_you_should_Keep_clean_teeth'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case3', This_rule_base, 'what_to_should',
                  num_case3, None,
                  (pattern.pattern_literal('You_got_Discoloration_teeth_Go_to_the_doctor_for_A_consultation'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case4', This_rule_base, 'what_to_should',
                  num_case4, None,
                  (pattern.pattern_literal('You_got_Discoloration_teeth_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case5', This_rule_base, 'what_to_should',
                  num_case5, None,
                  (pattern.pattern_literal('You_got_Discoloration_teeth_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case6', This_rule_base, 'what_to_should',
                  num_case6, None,
                  (pattern.pattern_literal('You_got_Discoloration_teeth_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case7', This_rule_base, 'what_to_should',
                  num_case7, None,
                  (pattern.pattern_literal('You_got_Discoloration_teeth_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case8', This_rule_base, 'what_to_should',
                  num_case8, None,
                  (pattern.pattern_literal('You_got_Discoloration_teeth_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case9', This_rule_base, 'what_to_should',
                  num_case9, None,
                  (pattern.pattern_literal('You_got_Discoloration_teeth_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_selection1', This_rule_base, 'what_to_should',
                  what_to_selection1, None,
                  (pattern.pattern_literal('Brush_your_teeth_after_drinking_black_drinks'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection2', This_rule_base, 'what_to_should',
                  what_to_selection2, None,
                  (pattern.pattern_literal('Apply_over_the_counter_whiteners_available_in_stick_on_strips_or_tooth_shaped_trays'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection3', This_rule_base, 'what_to_should',
                  what_to_selection3, None,
                  (pattern.pattern_literal('It_is_possible_that_your_teeth_have_changed_in_color_go_to_the_doctor'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection4', This_rule_base, 'what_to_should',
                  what_to_selection4, None,
                  (pattern.pattern_literal('Go_to_the_doctor_forA_consultation'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_you_have_Gingivitis_from_another_reson', This_rule_base, 'what_you_have',
                  what_you_have_Gingivitis_from_another_reson, None,
                  (pattern.pattern_literal('Gingivitis'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_you_have_Gingivitis_from_one_reson', This_rule_base, 'what_you_have',
                  what_you_have_Gingivitis_from_one_reson, None,
                  (pattern.pattern_literal('Gingivitis'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_you_havenot_Gingivitis', This_rule_base, 'what_you_have',
                  what_you_havenot_Gingivitis, None,
                  (pattern.pattern_literal('not_Gingivitis'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_you_have_Gingivitis', This_rule_base, 'what_you_have',
                  what_you_have_Gingivitis, None,
                  (pattern.pattern_literal('Gingivitis'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_you_have_periodontitis', This_rule_base, 'what_you_have',
                  what_you_have_periodontitis, None,
                  (pattern.pattern_literal('periodontitis'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_you_have_not_periodontitis', This_rule_base, 'what_you_have',
                  what_you_have_not_periodontitis, None,
                  (pattern.pattern_literal('not_periodontitis'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case00', This_rule_base, 'what_to_should',
                  num_case00, None,
                  (pattern.pattern_literal('Keep_clean_teeth_BY_Toothbrush'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case01', This_rule_base, 'what_to_should',
                  num_case01, None,
                  (pattern.pattern_literal('this_is_normal_however_Keep_clean_teeth_BY_Toothbrush'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case02', This_rule_base, 'what_to_should',
                  num_case02, None,
                  (pattern.pattern_literal('Thank_goodness_you_should_Keep_clean_teeth'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case03', This_rule_base, 'what_to_should',
                  num_case03, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case04', This_rule_base, 'what_to_should',
                  num_case04, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case05', This_rule_base, 'what_to_should',
                  num_case05, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case06', This_rule_base, 'what_to_should',
                  num_case06, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case07', This_rule_base, 'what_to_should',
                  num_case07, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case08', This_rule_base, 'what_to_should',
                  num_case08, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case09', This_rule_base, 'what_to_should',
                  num_case09, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_selection01', This_rule_base, 'what_to_should',
                  what_to_selection01, None,
                  (pattern.pattern_literal('Brush_your_teeth_after_eat_sugars'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection02', This_rule_base, 'what_to_should',
                  what_to_selection02, None,
                  (pattern.pattern_literal('Go_to_the_doctor_forA_consultation'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection03', This_rule_base, 'what_to_should',
                  what_to_selection03, None,
                  (pattern.pattern_literal('It_is_possible_that_your_teeth_have_cavities_go_to_the_doctor'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection11', This_rule_base, 'what_to_shou',
                  what_to_selection11, None,
                  (pattern.pattern_literal('Maybe_you_got_gumsHyperPlasia_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection12', This_rule_base, 'what_to_shou',
                  what_to_selection12, None,
                  (pattern.pattern_literal('Use_a_gum_rinser_and_it_will_get_better'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection13', This_rule_base, 'what_to_shou',
                  what_to_selection13, None,
                  (pattern.pattern_literal('It_is_possible_that_your_teeth_have_gumsHyperPlasia_go_to_the_doctor'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('num_case11', This_rule_base, 'what_to_shou',
                  num_case11, None,
                  (pattern.pattern_literal('your_gums_are_fine_Keep_clean_teeth_BY_Toothbrush'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case12', This_rule_base, 'what_to_shou',
                  num_case12, None,
                  (pattern.pattern_literal('It_is_that_your_teeth_have_gumsHyperPlasia_go_to_the_doctor'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case13', This_rule_base, 'what_to_shou',
                  num_case13, None,
                  (pattern.pattern_literal('Reduce_the_intake_of_these_medications_and_keep_your_teeth_clean_using_tooth_rinse'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case14', This_rule_base, 'what_to_shou',
                  num_case14, None,
                  (pattern.pattern_literal('Keep_clean_teeth_BY_Toothbrush_and_tooth_rinse_And_you_will_notice_improvement_in_your_gums'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case15', This_rule_base, 'what_to_shou',
                  num_case15, None,
                  (pattern.pattern_literal('There_may_be_other_reasons_for_bleeding_gums_consult_a_doctor'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case20', This_rule_base, 'what_to_should2',
                  num_case20, None,
                  (pattern.pattern_literal('Keep_clean_teeth_BY_Toothbrush'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case21', This_rule_base, 'what_to_should2',
                  num_case21, None,
                  (pattern.pattern_literal('this_is_normal_however_Keep_clean_teeth_BY_Toothbrush'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case22', This_rule_base, 'what_to_should2',
                  num_case22, None,
                  (pattern.pattern_literal('Thank_goodness_you_should_Keep_clean_teeth'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case23', This_rule_base, 'what_to_should2',
                  num_case23, None,
                  (pattern.pattern_literal('You_got_dental_abscess_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case24', This_rule_base, 'what_to_should2',
                  num_case24, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case25', This_rule_base, 'what_to_should2',
                  num_case25, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case26', This_rule_base, 'what_to_should2',
                  num_case26, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('num_case27', This_rule_base, 'what_to_should2',
                  num_case27, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case28', This_rule_base, 'what_to_should2',
                  num_case28, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('num_case29', This_rule_base, 'what_to_should2',
                  num_case29, None,
                  (pattern.pattern_literal('You_got_cavities_Go_to_the_doctor_forA_consultation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_selection21', This_rule_base, 'what_to_should2',
                  what_to_selection21, None,
                  (pattern.pattern_literal('Brush_your_teeth_softly'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection22', This_rule_base, 'what_to_should2',
                  what_to_selection22, None,
                  (pattern.pattern_literal('Avoid_food_and_drink_that_is_either_too_hot_or_too_cold'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection23', This_rule_base, 'what_to_should2',
                  what_to_selection23, None,
                  (pattern.pattern_literal('Go_to_the_doctor_for_a_consultion'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_selection24', This_rule_base, 'what_to_should2',
                  what_to_selection24, None,
                  (pattern.pattern_literal('It_is_possible_that_your_teeth_have_dental_abscess_go_to_the_doctor'),),
                  (),
                  (contexts.variable('ans'),))


Krb_filename = '..\\bc_simple_rules_questions.krb'
Krb_lineno_map = (
    ((14, 18), (3, 3)),
    ((20, 25), (5, 5)),
    ((38, 42), (8, 8)),
    ((44, 49), (10, 10)),
    ((62, 66), (13, 13)),
    ((68, 73), (15, 15)),
    ((74, 79), (16, 16)),
    ((80, 85), (17, 17)),
    ((98, 102), (20, 20)),
    ((104, 109), (22, 22)),
    ((110, 115), (23, 23)),
    ((116, 121), (24, 24)),
    ((134, 138), (27, 27)),
    ((140, 145), (29, 29)),
    ((146, 151), (30, 30)),
    ((152, 157), (31, 31)),
    ((170, 174), (34, 34)),
    ((176, 181), (36, 36)),
    ((182, 187), (37, 37)),
    ((188, 193), (38, 38)),
    ((206, 210), (41, 41)),
    ((212, 217), (43, 43)),
    ((218, 223), (44, 44)),
    ((224, 229), (45, 45)),
    ((242, 246), (48, 48)),
    ((248, 253), (50, 50)),
    ((254, 259), (51, 51)),
    ((260, 265), (52, 52)),
    ((278, 282), (55, 55)),
    ((284, 289), (57, 57)),
    ((290, 295), (58, 58)),
    ((296, 301), (59, 59)),
    ((314, 318), (62, 62)),
    ((320, 325), (64, 64)),
    ((326, 331), (65, 65)),
    ((332, 337), (66, 66)),
    ((350, 354), (70, 70)),
    ((356, 361), (72, 72)),
    ((362, 362), (73, 73)),
    ((375, 379), (76, 76)),
    ((381, 386), (78, 78)),
    ((387, 387), (79, 79)),
    ((400, 404), (83, 83)),
    ((406, 411), (85, 85)),
    ((412, 412), (86, 86)),
    ((425, 429), (89, 89)),
    ((431, 436), (91, 91)),
    ((437, 437), (92, 92)),
    ((450, 454), (100, 100)),
    ((456, 461), (102, 102)),
    ((474, 478), (105, 105)),
    ((480, 485), (107, 107)),
    ((498, 502), (110, 110)),
    ((504, 509), (112, 112)),
    ((510, 515), (113, 113)),
    ((528, 532), (116, 116)),
    ((534, 539), (118, 118)),
    ((540, 545), (119, 119)),
    ((558, 562), (123, 123)),
    ((564, 569), (125, 125)),
    ((570, 575), (126, 126)),
    ((588, 592), (129, 129)),
    ((594, 599), (131, 131)),
    ((600, 605), (132, 132)),
    ((618, 622), (145, 145)),
    ((624, 629), (147, 147)),
    ((642, 646), (150, 150)),
    ((648, 653), (152, 152)),
    ((666, 670), (155, 155)),
    ((672, 677), (157, 157)),
    ((678, 683), (158, 158)),
    ((684, 689), (159, 159)),
    ((702, 706), (162, 162)),
    ((708, 713), (164, 164)),
    ((714, 719), (165, 165)),
    ((720, 725), (166, 166)),
    ((738, 742), (169, 169)),
    ((744, 749), (171, 171)),
    ((750, 755), (172, 172)),
    ((756, 761), (173, 173)),
    ((774, 778), (175, 175)),
    ((780, 785), (177, 177)),
    ((786, 791), (178, 178)),
    ((792, 797), (179, 179)),
    ((810, 814), (181, 181)),
    ((816, 821), (183, 183)),
    ((822, 827), (184, 184)),
    ((828, 833), (185, 185)),
    ((846, 850), (187, 187)),
    ((852, 857), (189, 189)),
    ((858, 863), (190, 190)),
    ((864, 869), (191, 191)),
    ((882, 886), (193, 193)),
    ((888, 893), (195, 195)),
    ((894, 899), (196, 196)),
    ((900, 905), (197, 197)),
    ((918, 922), (199, 199)),
    ((924, 929), (201, 201)),
    ((930, 935), (202, 202)),
    ((936, 941), (203, 203)),
    ((954, 958), (206, 206)),
    ((960, 965), (208, 208)),
    ((966, 966), (209, 209)),
    ((979, 983), (212, 212)),
    ((985, 990), (214, 214)),
    ((991, 991), (215, 215)),
    ((1004, 1008), (218, 218)),
    ((1010, 1015), (221, 221)),
    ((1016, 1016), (222, 222)),
    ((1029, 1033), (225, 225)),
    ((1035, 1040), (227, 227)),
    ((1041, 1041), (228, 228)),
    ((1054, 1058), (231, 231)),
    ((1060, 1065), (233, 233)),
    ((1066, 1066), (234, 234)),
    ((1079, 1083), (237, 237)),
    ((1085, 1090), (240, 240)),
    ((1091, 1091), (241, 241)),
    ((1104, 1108), (243, 243)),
    ((1110, 1115), (245, 245)),
    ((1128, 1132), (247, 247)),
    ((1134, 1139), (249, 249)),
    ((1140, 1145), (250, 250)),
    ((1146, 1151), (251, 251)),
    ((1164, 1168), (253, 253)),
    ((1170, 1175), (255, 255)),
    ((1176, 1181), (256, 256)),
    ((1182, 1187), (257, 257)),
    ((1200, 1204), (259, 259)),
    ((1206, 1211), (261, 261)),
    ((1212, 1217), (262, 262)),
    ((1218, 1223), (263, 263)),
    ((1236, 1240), (265, 265)),
    ((1242, 1247), (267, 267)),
    ((1248, 1253), (268, 268)),
    ((1254, 1259), (269, 269)),
    ((1272, 1276), (272, 272)),
    ((1278, 1283), (274, 274)),
    ((1296, 1300), (277, 277)),
    ((1302, 1307), (279, 279)),
    ((1320, 1324), (282, 282)),
    ((1326, 1331), (284, 284)),
    ((1332, 1337), (285, 285)),
    ((1338, 1343), (286, 286)),
    ((1356, 1360), (289, 289)),
    ((1362, 1367), (291, 291)),
    ((1368, 1373), (292, 292)),
    ((1374, 1379), (293, 293)),
    ((1392, 1396), (296, 296)),
    ((1398, 1403), (298, 298)),
    ((1404, 1409), (299, 299)),
    ((1410, 1415), (300, 300)),
    ((1428, 1432), (302, 302)),
    ((1434, 1439), (304, 304)),
    ((1440, 1445), (305, 305)),
    ((1446, 1451), (306, 306)),
    ((1464, 1468), (308, 308)),
    ((1470, 1475), (310, 310)),
    ((1476, 1481), (311, 311)),
    ((1482, 1487), (312, 312)),
    ((1500, 1504), (314, 314)),
    ((1506, 1511), (316, 316)),
    ((1512, 1517), (317, 317)),
    ((1518, 1523), (318, 318)),
    ((1536, 1540), (320, 320)),
    ((1542, 1547), (322, 322)),
    ((1548, 1553), (323, 323)),
    ((1554, 1559), (324, 324)),
    ((1572, 1576), (326, 326)),
    ((1578, 1583), (328, 328)),
    ((1584, 1589), (329, 329)),
    ((1590, 1595), (330, 330)),
    ((1608, 1612), (333, 333)),
    ((1614, 1619), (335, 335)),
    ((1620, 1620), (336, 336)),
    ((1633, 1637), (339, 339)),
    ((1639, 1644), (341, 341)),
    ((1645, 1645), (342, 342)),
    ((1658, 1662), (345, 345)),
    ((1664, 1669), (347, 347)),
    ((1670, 1670), (348, 348)),
    ((1683, 1687), (351, 351)),
    ((1689, 1694), (353, 353)),
    ((1695, 1695), (354, 354)),
)

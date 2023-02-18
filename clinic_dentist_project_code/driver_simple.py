import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)




def dental_abscess():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('bc_simple_rules_questions')  # STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")

    try:
        with engine.prove_goal(
                'bc_simple_rules_questions.what_to_should($bring)') as gen:  # STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("You should: %s" % (vars['bring']))  # STUDENTS: you will need to edit this line

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")


#abdaltawab
def the_gums():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('bc_simple_rules_questions')  # STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")

    try:
        with engine.prove_goal(
                'bc_simple_rules_questions.what_you_have($bring)') as gen:  # STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("you have %s" % (vars['bring']))  # STUDENTS: you will need to edit this line
                print("informations and Tips and advice about the disease \n Gingivitis is a mild form of gum disease \n You can usually reverse it with: \n  1-daily brushing and flossing. \n  2-regular cleanings by a dentist or dental hygienist. \n  3- you must go to the doctor if it isnot stop bleeding \n but watch out Untreated gingivitis can lead to periodontitis like Leukemia, a type of blood cancer . ")
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")


def cariosity():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('bc_simple_rules_questions')  # STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")

    try:
        with engine.prove_goal(
                'bc_simple_rules_questions.what_to_should($bring)') as gen:  # STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("You should : %s" % (vars['bring']))  # STUDENTS: you will need to edit this line
                # print("You should clean teeth by tooth brush: %s" % (vars['bring']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")


def gumsHyperPlasia():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('bc_simple_rules_questions')  # STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")

    try:
        with engine.prove_goal(
                'bc_simple_rules_questions.what_to_shou($bring)') as gen:  # STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("You should : %s" % (vars['bring']))  # STUDENTS: you will need to edit this line
                # print("You should clean teeth by tooth brush: %s" % (vars['bring']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")


def discoloration_teeth():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('bc_simple_rules_questions')  # STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")

    try:
        with engine.prove_goal(
                'bc_simple_rules_questions.what_to_should2($bring)') as gen:  # STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("You should : %s" % (vars['bring']))  # STUDENTS: you will need to edit this line
                # print("You should clean teeth by tooth brush: %s" % (vars['bring']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")
name = input("enter your name ")
print("hello "+ name + "\n welcome in our program\n ")
print ("Where is the location of the disease in your mouth?\n1-Is it in the gums? \n2-dental abscess,\n3- cariosity teeth, \n4- gumsHyperPlasia bleeding in the mouth?\n5-discoloration_teeth?")



numper_disease= input("choose from the above list ")
print(numper_disease)
if numper_disease == '1':
    the_gums()
elif numper_disease == '2':
    dental_abscess()
elif numper_disease == '3':
    cariosity()
elif numper_disease == '4':
    gumsHyperPlasia()
elif numper_disease == '5':
    discoloration_teeth()
#bc_test_questions()


#the_gums()


















#abdaltawab
#import contextlib
# import sys
#
# from pyke import knowledge_engine
# from pyke import krb_traceback
#
# engine = knowledge_engine.engine(__file__)
#
# #
# # def bc_test():
# #     engine.reset()  # Allows us to run tests multiple times.
# #
# #     engine.activate('bc_simple_rules')  # STUDENTS: you will need to edit the name of your rule file here
# #
# #     print("doing proof")
# #
# #     try:
# #         with engine.prove_goal(
# #                 'bc_simple_rules.what_you_have($bring)') as gen:  # STUDENTS: you will need to edit this line
# #             for vars, plan in gen:
# #                 print("You should bring: %s" % (vars['bring']))  # STUDENTS: you will need to edit this line
# #     except Exception:
# #         # This converts stack frames of generated python functions back to the
# #         # .krb file.
# #         krb_traceback.print_exc()
# #         sys.exit(1)
# #
# #     print()
# #     print("done")
#     # engine.print_stats()
#
#
# def bc_test_questions():
#     engine.reset()  # Allows us to run tests multiple times.
#
#     engine.activate('bc_simple_rules_questions')  # STUDENTS: you will need to edit the name of your rule file here
#
#     print("doing proof")
#
#     try:
#         with engine.prove_goal(
#                 'bc_simple_rules_questions.what_you_have($bring)') as gen:  # STUDENTS: you will need to edit this line
#             for vars, plan in gen:
#                 print("you have %s" % (vars['bring']))  # STUDENTS: you will need to edit this line
#                 print("informations and Tips and advice about the disease \n Gingivitis is a mild form of gum disease \n You can usually reverse it with: \n  1-daily brushing and flossing. \n  2-regular cleanings by a dentist or dental hygienist. \n  3- you must go to the doctor if it isnot stop bleeding \n but watch out Untreated gingivitis can lead to periodontitis like Leukemia, a type of blood cancer . ")
#     except Exception:
#         # This converts stack frames of generated python functions back to the
#         # .krb file.
#         krb_traceback.print_exc()
#         sys.exit(1)
#
#     print()
#     print("done")
# bc_test_questions()
#






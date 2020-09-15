"""
Solutions of the rocket assignment to compare with student answers.
"""


def hw1_answer1(val):
    ans, tol = 70.0, 1e-2
    return abs(val - ans) <= tol


def hw1_answer2(val):
    ans, tol = 126.7410, 1e-2
    return abs(val - ans) <= tol


def hw1_answer3(val):
    ans, tol = 4.0, 1e-2
    return abs(val - ans) <= tol


def hw1_answer4(val):
    ans, tol = 237.6928, 1e-2
    return abs(val - ans) <= tol


def hw1_answer5(val):
    ans, tol = 771.8390, 1e-2
    return abs(val - ans) <= tol


def hw1_answer6(val):
    ans, tol = 13.75, 1e-2
    return abs(val - ans) <= tol


def hw1_answer7(val):
    ans, tol = 27.5365, 1e-2
    return abs(val - ans) <= tol


def hw1_answer8(val):
    ans, tol = -94.7193, 1e-2
    return abs(val - ans) <= tol


dispatcher = {'hw1_answer1': hw1_answer1, 'hw1_answer2': hw1_answer2,
              'hw1_answer3': hw1_answer3, 'hw1_answer4': hw1_answer4,
              'hw1_answer5': hw1_answer5, 'hw1_answer6': hw1_answer6,
              'hw1_answer7': hw1_answer7, 'hw1_answer8': hw1_answer8}


def check(funcname, val,
          print_res=True, return_res=False):
  res = dispatcher[funcname](val)
  if print_res:
    res_str = 'Good job!' if res else 'Try again!'
    print('[{}] {}'.format(funcname, res_str))
  if return_res:
    return res

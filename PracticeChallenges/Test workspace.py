
def nums(numbers):
    one = """
     *
     *
     *
     *
     *
    """
    two = """
    ***
      *
    ***
    *
    ***
    """
    three = """
    ***
      *
    ***
      *
    ***
    """
    four = """
    * *
    * *
    ***
      *
      *
    """
    five = """
    ***
    *
    ***
      *
    ***
    """
    six = """
    **
    *
    ***
    * *
    ***
    """
    seven = """
    ***
      *
      *
      *
      *
    """
    eight = """
    ***
    * *
    ***
    * *
    ***
    """
    nine = """
    ***
    * *
    ***
      *
      *
    """
    zero = """
    ***
    * *
    * *
    * *
    ***
    """
    nums ={
        1 : one,
        2 : two,
        3 : three,
        4 : four,
        5 : five,
        6 : six,
        7 : seven,
        8 : eight,
        9 : nine,
        0 : zero
    }
    for num in str(numbers):
        print(nums[int(num)])
nums(123)
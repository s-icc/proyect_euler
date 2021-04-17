"""

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""


nums = ["One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
        "Twenty",
        "Twenty-one",
        "Twenty-two",
        "Twenty-three",
        "Twenty-four",
        "Twenty-five",
        "Twenty-six",
        "Twenty-seven",
        "Twenty-eight",
        "Twenty-nine",
        "Thirty",
        "Thirty-one",
        "Thirty-two",
        "Thirty-three",
        "Thirty-four",
        "Thirty-five",
        "Thirty-six",
        "Thirty-seven",
        "Thirty-eight",
        "Thirty-nine",
        "Forty",
        "Forty-one",
        "Forty-two",
        "Forty-three",
        "Forty-four",
        "Forty-five",
        "Forty-six",
        "Forty-seven",
        "Forty-eight",
        "Forty-nine",
        "Fifty",
        "Fifty-one",
        "Fifty-two",
        "Fifty-three",
        "Fifty-four",
        "Fifty-five",
        "Fifty-six",
        "Fifty-seven",
        "Fifty-eight",
        "Fifty-nine",
        "Sixty",
        "Sixty-one",
        "Sixty-two",
        "Sixty-three",
        "Sixty-four",
        "Sixty-five",
        "Sixty-six",
        "Sixty-seven",
        "Sixty-eight",
        "Sixty-nine",
        "Seventy",
        "Seventy-one",
        "Seventy-two",
        "Seventy-three",
        "Seventy-four",
        "Seventy-five",
        "Seventy-six",
        "Seventy-seven",
        "Seventy-eight",
        "Seventy-nine",
        "Eighty",
        "Eighty-one",
        "Eighty-two",
        "Eighty-three",
        "Eighty-four",
        "Eighty-five",
        "Eighty-six",
        "Eighty-seven",
        "Eighty-eight",
        "Eighty-nine",
        "Ninety",
        "Ninety-one",
        "Ninety-two",
        "Ninety-three",
        "Ninety-four",
        "Ninety-five",
        "Ninety-six",
        "Ninety-seven",
        "Ninety-eight",
        "Ninety-nine",
        "One Hundred",
        "One Hundred and One",
        "One Hundred and Two",
        "One Hundred and Three",
        "One Hundred and Four",
        "One Hundred and Five",
        "One Hundred and Six",
        "One Hundred and Seven",
        "One Hundred and Eight",
        "One Hundred and Nine",
        "One Hundred and Ten",
        "One Hundred and Eleven",
        "One Hundred and Twelve",
        "One Hundred and Thirteen",
        "One Hundred and Fourteen",
        "One Hundred and Fifteen",
        "One Hundred and Sixteen",
        "One Hundred and Seventeen",
        "One Hundred and Eighteen",
        "One Hundred and Nineteen",
        "One Hundred and Twenty",
        "One Hundred and Twenty One",
        "One Hundred and Twenty Two",
        "One Hundred and Twenty Three",
        "One Hundred and Twenty Four",
        "One Hundred and Twenty Five",
        "One hundred and twenty-Six",
        "One hundred and twenty-Seven",
        "One hundred and twenty-Eight",
        "One hundred and twenty-Nine",
        "One hundred and thirty",
        "One hundred and thirty-One",
        "One hundred and thirty-Two",
        "One hundred and thirty-Three",
        "One hundred and thirty-Four",
        "One hundred and thirty-Five",
        "One hundred and thirty-Six",
        "One hundred and thirty-Seven",
        "One hundred and thirty-Eight",
        "One hundred and thirty-Nine",
        "One hundred and forty",
        "One hundred and forty-One",
        "One hundred and forty-Two",
        "One hundred and forty-Three",
        "One hundred and forty-Four",
        "One hundred and forty-Five",
        "One hundred and forty-Six",
        "One hundred and forty-Seven",
        "One hundred and forty-Eight",
        "One hundred and forty-Nine",
        "One hundred and fifty",
        "One hundred and fifty-One",
        "One hundred and fifty-Two",
        "One hundred and fifty-Three",
        "One hundred and fifty-Four",
        "One hundred and fifty-Five",
        "One hundred and fifty-Six",
        "One hundred and fifty-Seven",
        "One hundred and fifty-Eight",
        "One hundred and fifty-Nine",
        "One hundred and Sixty",
        "One hundred and Sixty-One",
        "One hundred and Sixty-Two",
        "One hundred and Sixty-Three",
        "One hundred and Sixty-Four",
        "One hundred and Sixty-Five",
        "One hundred and Sixty-Six",
        "One hundred and Sixty-Seven",
        "One hundred and Sixty-Eight",
        "One hundred and Sixty-Nine",
        "One hundred and Seventy",
        "One hundred and Seventy-One",
        "One hundred and Seventy-Two",
        "One hundred and Seventy-Three",
        "One hundred and Seventy-Four",
        "One hundred and Seventy-Five",
        "One hundred and Seventy-Six",
        "One hundred and Seventy-Seven",
        "One hundred and Seventy-Eight",
        "One hundred and Seventy-Nine",
        "One hundred and eighty",
        "One hundred and eighty-One",
        "One hundred and eighty-Two",
        "One hundred and eighty-Three",
        "One hundred and eighty-Four",
        "One hundred and eighty-Five",
        "One hundred and eighty-Six",
        "One hundred and eighty-Seven",
        "One hundred and eighty-Eight",
        "One hundred and eighty-Nine",
        "One hundred and Ninety",
        "One hundred and Ninety-One",
        "One hundred and Ninety-Two",
        "One hundred and Ninety-Three",
        "One hundred and Ninety-Four",
        "One hundred and Ninety-Five",
        "One hundred and Ninety-Six",
        "One hundred and Ninety-Seven",
        "One hundred and Ninety-Eight",
        "One hundred and Ninety-Nine",
        "Two hundred",
        "Two hundred and One",
        "Two hundred and Two",
        "Two hundred and Three",
        "Two hundred and Four",
        "Two hundred and Five",
        "Two hundred and Six",
        "Two hundred and Seven",
        "Two hundred and Eight",
        "Two hundred and Nine",
        "Two hundred and ten",
        "Two hundred and eleven",
        "Two hundred and twelve",
        "Two hundred and thirteen",
        "Two hundred and Fourteen",
        "Two hundred and fifteen",
        "Two hundred and Sixteen",
        "Two hundred and Seventeen",
        "Two hundred and eighteen",
        "Two hundred and Nineteen",
        "Two hundred and twenty",
        "Two hundred and twenty-One",
        "Two hundred and twenty-Two",
        "Two hundred and twenty-Three",
        "Two hundred and twenty-Four",
        "Two hundred and twenty-Five",
        "Two hundred and twenty-Six",
        "Two hundred and twenty-Seven",
        "Two hundred and twenty-Eight",
        "Two hundred and twenty-Nine",
        "Two hundred and thirty",
        "Two hundred and thirty-One",
        "Two hundred and thirty-Two",
        "Two hundred and thirty-Three",
        "Two hundred and thirty-Four",
        "Two hundred and thirty-Five",
        "Two hundred and thirty-Six",
        "Two hundred and thirty-Seven",
        "Two hundred and thirty-Eight",
        "Two hundred and thirty-Nine",
        "Two hundred and forty",
        "Two hundred and forty-One",
        "Two hundred and forty-Two",
        "Two hundred and forty-Three",
        "Two hundred and forty-Four",
        "Two hundred and forty-Five",
        "Two hundred and forty-Six",
        "Two hundred and forty-Seven",
        "Two hundred and forty-Eight",
        "Two hundred and forty-Nine",
        "Two hundred and fifty",
        "Two hundred and fifty-One",
        "Two hundred and fifty-Two",
        "Two hundred and fifty-Three",
        "Two hundred and fifty-Four",
        "Two hundred and fifty-Five",
        "Two hundred and fifty-Six",
        "Two hundred and fifty-Seven",
        "Two hundred and fifty-Eight",
        "Two hundred and fifty-Nine",
        "Two hundred and Sixty",
        "Two hundred and Sixty-One",
        "Two hundred and Sixty-Two",
        "Two hundred and Sixty-Three",
        "Two hundred and Sixty-Four",
        "Two hundred and Sixty-Five",
        "Two hundred and Sixty-Six",
        "Two hundred and Sixty-Seven",
        "Two hundred and Sixty-Eight",
        "Two hundred and Sixty-Nine",
        "Two hundred and Seventy",
        "Two hundred and Seventy-One",
        "Two hundred and Seventy-Two",
        "Two hundred and Seventy-Three",
        "Two hundred and Seventy-Four",
        "Two hundred and Seventy-Five",
        "Two hundred and Seventy-Six",
        "Two hundred and Seventy-Seven",
        "Two hundred and Seventy-Eight",
        "Two hundred and Seventy-Nine",
        "Two hundred and eighty",
        "Two hundred and eighty-One",
        "Two hundred and eighty-Two",
        "Two hundred and eighty-Three",
        "Two hundred and eighty-Four",
        "Two hundred and eighty-Five",
        "Two hundred and eighty-Six",
        "Two hundred and eighty-Seven",
        "Two hundred and eighty-Eight",
        "Two hundred and eighty-Nine",
        "Two hundred and Ninety",
        "Two hundred and Ninety-One",
        "Two hundred and Ninety-Two",
        "Two hundred and Ninety-Three",
        "Two hundred and Ninety-Four",
        "Two hundred and Ninety-Five",
        "Two hundred and Ninety-Six",
        "Two hundred and Ninety-Seven",
        "Two hundred and Ninety-Eight",
        "Two hundred and Ninety-Nine",
        "Three hundred",
        "Three hundred and One",
        "Three hundred and Two",
        "Three hundred and Three",
        "Three hundred and Four",
        "Three hundred and Five",
        "Three hundred and Six",
        "Three hundred and Seven",
        "Three hundred and Eight",
        "Three hundred and Nine",
        "Three hundred and ten",
        "Three hundred and eleven",
        "Three hundred and twelve",
        "Three hundred and thirteen",
        "Three hundred and Fourteen",
        "Three hundred and fifteen",
        "Three hundred and Sixteen",
        "Three hundred and Seventeen",
        "Three hundred and eighteen",
        "Three hundred and Nineteen",
        "Three hundred and twenty",
        "Three hundred and twenty-One",
        "Three hundred and twenty-Two",
        "Three hundred and twenty-Three",
        "Three hundred and twenty-Four",
        "Three hundred and twenty-Five",
        "Three hundred and twenty-Six",
        "Three hundred and twenty-Seven",
        "Three hundred and twenty-Eight",
        "Three hundred and twenty-Nine",
        "Three hundred and thirty",
        "Three hundred and thirty-One",
        "Three hundred and thirty-Two",
        "Three hundred and thirty-Three",
        "Three hundred and thirty-Four",
        "Three hundred and thirty-Five",
        "Three hundred and thirty-Six",
        "Three hundred and thirty-Seven",
        "Three hundred and thirty-Eight",
        "Three hundred and thirty-Nine",
        "Three hundred and forty",
        "Three hundred and forty-One",
        "Three hundred and forty-Two",
        "Three hundred and forty-Three",
        "Three hundred and forty-Four",
        "Three hundred and forty-Five",
        "Three hundred and forty-Six",
        "Three hundred and forty-Seven",
        "Three hundred and forty-Eight",
        "Three hundred and forty-Nine",
        "Three hundred and fifty",
        "Three hundred and fifty-One",
        "Three hundred and fifty-Two",
        "Three hundred and fifty-Three",
        "Three hundred and fifty-Four",
        "Three hundred and fifty-Five",
        "Three hundred and fifty-Six",
        "Three hundred and fifty-Seven",
        "Three hundred and fifty-Eight",
        "Three hundred and fifty-Nine",
        "Three hundred and Sixty",
        "Three hundred and Sixty-One",
        "Three hundred and Sixty-Two",
        "Three hundred and Sixty-Three",
        "Three hundred and Sixty-Four",
        "Three hundred and Sixty-Five",
        "Three hundred and Sixty-Six",
        "Three hundred and Sixty-Seven",
        "Three hundred and Sixty-Eight",
        "Three hundred and Sixty-Nine",
        "Three hundred and Seventy",
        "Three hundred and Seventy-One",
        "Three hundred and Seventy-Two",
        "Three hundred and Seventy-Three",
        "Three hundred and Seventy-Four",
        "Three hundred and Seventy-Five",
        "Three hundred and Seventy-Six",
        "Three hundred and Seventy-Seven",
        "Three hundred and Seventy-Eight",
        "Three hundred and Seventy-Nine",
        "Three hundred and eighty",
        "Three hundred and eighty-One",
        "Three hundred and eighty-Two",
        "Three hundred and eighty-Three",
        "Three hundred and eighty-Four",
        "Three hundred and eighty-Five",
        "Three hundred and eighty-Six",
        "Three hundred and eighty-Seven",
        "Three hundred and eighty-Eight",
        "Three hundred and eighty-Nine",
        "Three hundred and Ninety",
        "Three hundred and Ninety-One",
        "Three hundred and Ninety-Two",
        "Three hundred and Ninety-Three",
        "Three hundred and Ninety-Four",
        "Three hundred and Ninety-Five",
        "Three hundred and Ninety-Six",
        "Three hundred and Ninety-Seven",
        "Three hundred and Ninety-Eight",
        "Three hundred and Ninety-Nine",
        "Four hundred",
        "Four hundred and One",
        "Four hundred and Two",
        "Four hundred and Three",
        "Four hundred and Four",
        "Four hundred and Five",
        "Four hundred and Six",
        "Four hundred and Seven",
        "Four hundred and Eight",
        "Four hundred and Nine",
        "Four hundred and ten",
        "Four hundred and eleven",
        "Four hundred and twelve",
        "Four hundred and thirteen",
        "Four hundred and Fourteen",
        "Four hundred and fifteen",
        "Four hundred and Sixteen",
        "Four hundred and Seventeen",
        "Four hundred and eighteen",
        "Four hundred and Nineteen",
        "Four hundred and twenty",
        "Four hundred and twenty-One",
        "Four hundred and twenty-Two",
        "Four hundred and twenty-Three",
        "Four hundred and twenty-Four",
        "Four hundred and twenty-Five",
        "Four hundred and twenty-Six",
        "Four hundred and twenty-Seven",
        "Four hundred and twenty-Eight",
        "Four hundred and twenty-Nine",
        "Four hundred and thirty",
        "Four hundred and thirty-One",
        "Four hundred and thirty-Two",
        "Four hundred and thirty-Three",
        "Four hundred and thirty-Four",
        "Four hundred and thirty-Five",
        "Four hundred and thirty-Six",
        "Four hundred and thirty-Seven",
        "Four hundred and thirty-Eight",
        "Four hundred and thirty-Nine",
        "Four hundred and forty",
        "Four hundred and forty-One",
        "Four hundred and forty-Two",
        "Four hundred and forty-Three",
        "Four hundred and forty-Four",
        "Four hundred and forty-Five",
        "Four hundred and forty-Six",
        "Four hundred and forty-Seven",
        "Four hundred and forty-Eight",
        "Four hundred and forty-Nine",
        "Four hundred and fifty",
        "Four hundred and fifty-One",
        "Four hundred and fifty-Two",
        "Four hundred and fifty-Three",
        "Four hundred and fifty-Four",
        "Four hundred and fifty-Five",
        "Four hundred and fifty-Six",
        "Four hundred and fifty-Seven",
        "Four hundred and fifty-Eight",
        "Four hundred and fifty-Nine",
        "Four hundred and Sixty",
        "Four hundred and Sixty-One",
        "Four hundred and Sixty-Two",
        "Four hundred and Sixty-Three",
        "Four hundred and Sixty-Four",
        "Four hundred and Sixty-Five",
        "Four hundred and Sixty-Six",
        "Four hundred and Sixty-Seven",
        "Four hundred and Sixty-Eight",
        "Four hundred and Sixty-Nine",
        "Four hundred and Seventy",
        "Four hundred and Seventy-One",
        "Four hundred and Seventy-Two",
        "Four hundred and Seventy-Three",
        "Four hundred and Seventy-Four",
        "Four hundred and Seventy-Five",
        "Four hundred and Seventy-Six",
        "Four hundred and Seventy-Seven",
        "Four hundred and Seventy-Eight",
        "Four hundred and Seventy-Nine",
        "Four hundred and eighty",
        "Four hundred and eighty-One",
        "Four hundred and eighty-Two",
        "Four hundred and eighty-Three",
        "Four hundred and eighty-Four",
        "Four hundred and eighty-Five",
        "Four hundred and eighty-Six",
        "Four hundred and eighty-Seven",
        "Four hundred and eighty-Eight",
        "Four hundred and eighty-Nine",
        "Four hundred and Ninety",
        "Four hundred and Ninety-One",
        "Four hundred and Ninety-Two",
        "Four hundred and Ninety-Three",
        "Four hundred and Ninety-Four",
        "Four hundred and Ninety-Five",
        "Four hundred and Ninety-Six",
        "Four hundred and Ninety-Seven",
        "Four hundred and Ninety-Eight",
        "Four hundred and Ninety-Nine",
        "Five hundred",
        "Five hundred and One",
        "Five hundred and Two",
        "Five hundred and Three",
        "Five hundred and Four",
        "Five hundred and Five",
        "Five hundred and Six",
        "Five hundred and Seven",
        "Five hundred and Eight",
        "Five hundred and Nine",
        "Five hundred and ten",
        "Five hundred and eleven",
        "Five hundred and twelve",
        "Five hundred and thirteen",
        "Five hundred and Fourteen",
        "Five hundred and fifteen",
        "Five hundred and Sixteen",
        "Five hundred and Seventeen",
        "Five hundred and eighteen",
        "Five hundred and Nineteen",
        "Five hundred and twenty",
        "Five hundred and twenty-One",
        "Five hundred and twenty-Two",
        "Five hundred and twenty-Three",
        "Five hundred and twenty-Four",
        "Five hundred and twenty-Five",
        "Five hundred and twenty-Six",
        "Five hundred and twenty-Seven",
        "Five hundred and twenty-Eight",
        "Five hundred and twenty-Nine",
        "Five hundred and thirty",
        "Five hundred and thirty-One",
        "Five hundred and thirty-Two",
        "Five hundred and thirty-Three",
        "Five hundred and thirty-Four",
        "Five hundred and thirty-Five",
        "Five hundred and thirty-Six",
        "Five hundred and thirty-Seven",
        "Five hundred and thirty-Eight",
        "Five hundred and thirty-Nine",
        "Five hundred and forty",
        "Five hundred and forty-One",
        "Five hundred and forty-Two",
        "Five hundred and forty-Three",
        "Five hundred and forty-Four",
        "Five hundred and forty-Five",
        "Five hundred and forty-Six",
        "Five hundred and forty-Seven",
        "Five hundred and forty-Eight",
        "Five hundred and forty-Nine",
        "Five hundred and fifty",
        "Five hundred and fifty-One",
        "Five hundred and fifty-Two",
        "Five hundred and fifty-Three",
        "Five hundred and fifty-Four",
        "Five hundred and fifty-Five",
        "Five hundred and fifty-Six",
        "Five hundred and fifty-Seven",
        "Five hundred and fifty-Eight",
        "Five hundred and fifty-Nine",
        "Five hundred and Sixty",
        "Five hundred and Sixty-One",
        "Five hundred and Sixty-Two",
        "Five hundred and Sixty-Three",
        "Five hundred and Sixty-Four",
        "Five hundred and Sixty-Five",
        "Five hundred and Sixty-Six",
        "Five hundred and Sixty-Seven",
        "Five hundred and Sixty-Eight",
        "Five hundred and Sixty-Nine",
        "Five hundred and Seventy",
        "Five hundred and Seventy-One",
        "Five hundred and Seventy-Two",
        "Five hundred and Seventy-Three",
        "Five hundred and Seventy-Four",
        "Five hundred and Seventy-Five",
        "Five hundred and Seventy-Six",
        "Five hundred and Seventy-Seven",
        "Five hundred and Seventy-Eight",
        "Five hundred and Seventy-Nine",
        "Five hundred and eighty",
        "Five hundred and eighty-One",
        "Five hundred and eighty-Two",
        "Five hundred and eighty-Three",
        "Five hundred and eighty-Four",
        "Five hundred and eighty-Five",
        "Five hundred and eighty-Six",
        "Five hundred and eighty-Seven",
        "Five hundred and eighty-Eight",
        "Five hundred and eighty-Nine",
        "Five hundred and Ninety",
        "Five hundred and Ninety-One",
        "Five hundred and Ninety-Two",
        "Five hundred and Ninety-Three",
        "Five hundred and Ninety-Four",
        "Five hundred and Ninety-Five",
        "Five hundred and Ninety-Six",
        "Five hundred and Ninety-Seven",
        "Five hundred and Ninety-Eight",
        "Five hundred and Ninety-Nine",
        "Six hundred",
        "Six hundred and One",
        "Six hundred and Two",
        "Six hundred and Three",
        "Six hundred and Four",
        "Six hundred and Five",
        "Six hundred and Six",
        "Six hundred and Seven",
        "Six hundred and Eight",
        "Six hundred and Nine",
        "Six hundred and ten",
        "Six hundred and eleven",
        "Six hundred and twelve",
        "Six hundred and thirteen",
        "Six hundred and Fourteen",
        "Six hundred and fifteen",
        "Six hundred and Sixteen",
        "Six hundred and Seventeen",
        "Six hundred and eighteen",
        "Six hundred and Nineteen",
        "Six hundred and twenty",
        "Six hundred and twenty-One",
        "Six hundred and twenty-Two",
        "Six hundred and twenty-Three",
        "Six hundred and twenty-Four",
        "Six hundred and twenty-Five",
        "Six hundred and twenty-Six",
        "Six hundred and twenty-Seven",
        "Six hundred and twenty-Eight",
        "Six hundred and twenty-Nine",
        "Six hundred and thirty",
        "Six hundred and thirty-One",
        "Six hundred and thirty-Two",
        "Six hundred and thirty-Three",
        "Six hundred and thirty-Four",
        "Six hundred and thirty-Five",
        "Six hundred and thirty-Six",
        "Six hundred and thirty-Seven",
        "Six hundred and thirty-Eight",
        "Six hundred and thirty-Nine",
        "Six hundred and forty",
        "Six hundred and forty-One",
        "Six hundred and forty-Two",
        "Six hundred and forty-Three",
        "Six hundred and forty-Four",
        "Six hundred and forty-Five",
        "Six hundred and forty-Six",
        "Six hundred and forty-Seven",
        "Six hundred and forty-Eight",
        "Six hundred and forty-Nine",
        "Six hundred and fifty",
        "Six hundred and fifty-One",
        "Six hundred and fifty-Two",
        "Six hundred and fifty-Three",
        "Six hundred and fifty-Four",
        "Six hundred and fifty-Five",
        "Six hundred and fifty-Six",
        "Six hundred and fifty-Seven",
        "Six hundred and fifty-Eight",
        "Six hundred and fifty-Nine",
        "Six hundred and Sixty",
        "Six hundred and Sixty-One",
        "Six hundred and Sixty-Two",
        "Six hundred and Sixty-Three",
        "Six hundred and Sixty-Four",
        "Six hundred and Sixty-Five",
        "Six hundred and Sixty-Six",
        "Six hundred and Sixty-Seven",
        "Six hundred and Sixty-Eight",
        "Six hundred and Sixty-Nine",
        "Six hundred and Seventy",
        "Six hundred and Seventy-One",
        "Six hundred and Seventy-Two",
        "Six hundred and Seventy-Three",
        "Six hundred and Seventy-Four",
        "Six hundred and Seventy-Five",
        "Six hundred and Seventy-Six",
        "Six hundred and Seventy-Seven",
        "Six hundred and Seventy-Eight",
        "Six hundred and Seventy-Nine",
        "Six hundred and eighty",
        "Six hundred and eighty-One",
        "Six hundred and eighty-Two",
        "Six hundred and eighty-Three",
        "Six hundred and eighty-Four",
        "Six hundred and eighty-Five",
        "Six hundred and eighty-Six",
        "Six hundred and eighty-Seven",
        "Six hundred and eighty-Eight",
        "Six hundred and eighty-Nine",
        "Six hundred and Ninety",
        "Six hundred and Ninety-One",
        "Six hundred and Ninety-Two",
        "Six hundred and Ninety-Three",
        "Six hundred and Ninety-Four",
        "Six hundred and Ninety-Five",
        "Six hundred and Ninety-Six",
        "Six hundred and Ninety-Seven",
        "Six hundred and Ninety-Eight",
        "Six hundred and Ninety-Nine",
        "Seven hundred",
        "Seven hundred and One",
        "Seven hundred and Two",
        "Seven hundred and Three",
        "Seven hundred and Four",
        "Seven hundred and Five",
        "Seven hundred and Six",
        "Seven hundred and Seven",
        "Seven hundred and Eight",
        "Seven hundred and Nine",
        "Seven hundred and ten",
        "Seven hundred and eleven",
        "Seven hundred and twelve",
        "Seven hundred and thirteen",
        "Seven hundred and Fourteen",
        "Seven hundred and fifteen",
        "Seven hundred and Sixteen",
        "Seven hundred and Seventeen",
        "Seven hundred and eighteen",
        "Seven hundred and Nineteen",
        "Seven hundred and twenty",
        "Seven hundred and twenty-One",
        "Seven hundred and twenty-Two",
        "Seven hundred and twenty-Three",
        "Seven hundred and twenty-Four",
        "Seven hundred and twenty-Five",
        "Seven hundred and twenty-Six",
        "Seven hundred and twenty-Seven",
        "Seven hundred and twenty-Eight",
        "Seven hundred and twenty-Nine",
        "Seven hundred and thirty",
        "Seven hundred and thirty-One",
        "Seven hundred and thirty-Two",
        "Seven hundred and thirty-Three",
        "Seven hundred and thirty-Four",
        "Seven hundred and thirty-Five",
        "Seven hundred and thirty-Six",
        "Seven hundred and thirty-Seven",
        "Seven hundred and thirty-Eight",
        "Seven hundred and thirty-Nine",
        "Seven hundred and forty",
        "Seven hundred and forty-One",
        "Seven hundred and forty-Two",
        "Seven hundred and forty-Three",
        "Seven hundred and forty-Four",
        "Seven hundred and forty-Five",
        "Seven hundred and forty-Six",
        "Seven hundred and forty-Seven",
        "Seven hundred and forty-Eight",
        "Seven hundred and forty-Nine",
        "Seven hundred and fifty",
        "Seven hundred and fifty-One",
        "Seven hundred and fifty-Two",
        "Seven hundred and fifty-Three",
        "Seven hundred and fifty-Four",
        "Seven hundred and fifty-Five",
        "Seven hundred and fifty-Six",
        "Seven hundred and fifty-Seven",
        "Seven hundred and fifty-Eight",
        "Seven hundred and fifty-Nine",
        "Seven hundred and Sixty",
        "Seven hundred and Sixty-One",
        "Seven hundred and Sixty-Two",
        "Seven hundred and Sixty-Three",
        "Seven hundred and Sixty-Four",
        "Seven hundred and Sixty-Five",
        "Seven hundred and Sixty-Six",
        "Seven hundred and Sixty-Seven",
        "Seven hundred and Sixty-Eight",
        "Seven hundred and Sixty-Nine",
        "Seven hundred and Seventy",
        "Seven hundred and Seventy-One",
        "Seven hundred and Seventy-Two",
        "Seven hundred and Seventy-Three",
        "Seven hundred and Seventy-Four",
        "Seven hundred and Seventy-Five",
        "Seven hundred and Seventy-Six",
        "Seven hundred and Seventy-Seven",
        "Seven hundred and Seventy-Eight",
        "Seven hundred and Seventy-Nine",
        "Seven hundred and eighty",
        "Seven hundred and eighty-One",
        "Seven hundred and eighty-Two",
        "Seven hundred and eighty-Three",
        "Seven hundred and eighty-Four",
        "Seven hundred and eighty-Five",
        "Seven hundred and eighty-Six",
        "Seven hundred and eighty-Seven",
        "Seven hundred and eighty-Eight",
        "Seven hundred and eighty-Nine",
        "Seven hundred and Ninety",
        "Seven hundred and Ninety-One",
        "Seven hundred and Ninety-Two",
        "Seven hundred and Ninety-Three",
        "Seven hundred and Ninety-Four",
        "Seven hundred and Ninety-Five",
        "Seven hundred and Ninety-Six",
        "Seven hundred and Ninety-Seven",
        "Seven hundred and Ninety-Eight",
        "Seven hundred and Ninety-Nine",
        "Eight hundred",
        "Eight hundred and One",
        "Eight hundred and Two",
        "Eight hundred and Three",
        "Eight hundred and Four",
        "Eight hundred and Five",
        "Eight hundred and Six",
        "Eight hundred and Seven",
        "Eight hundred and Eight",
        "Eight hundred and Nine",
        "Eight hundred and ten",
        "Eight hundred and eleven",
        "Eight hundred and twelve",
        "Eight hundred and thirteen",
        "Eight hundred and Fourteen",
        "Eight hundred and fifteen",
        "Eight hundred and Sixteen",
        "Eight hundred and Seventeen",
        "Eight hundred and eighteen",
        "Eight hundred and Nineteen",
        "Eight hundred and twenty",
        "Eight hundred and twenty-One",
        "Eight hundred and twenty-Two",
        "Eight hundred and twenty-Three",
        "Eight hundred and twenty-Four",
        "Eight hundred and twenty-Five",
        "Eight hundred and twenty-Six",
        "Eight hundred and twenty-Seven",
        "Eight hundred and twenty-Eight",
        "Eight hundred and twenty-Nine",
        "Eight hundred and thirty",
        "Eight hundred and thirty-One",
        "Eight hundred and thirty-Two",
        "Eight hundred and thirty-Three",
        "Eight hundred and thirty-Four",
        "Eight hundred and thirty-Five",
        "Eight hundred and thirty-Six",
        "Eight hundred and thirty-Seven",
        "Eight hundred and thirty-Eight",
        "Eight hundred and thirty-Nine",
        "Eight hundred and forty",
        "Eight hundred and forty-One",
        "Eight hundred and forty-Two",
        "Eight hundred and forty-Three",
        "Eight hundred and forty-Four",
        "Eight hundred and forty-Five",
        "Eight hundred and forty-Six",
        "Eight hundred and forty-Seven",
        "Eight hundred and forty-Eight",
        "Eight hundred and forty-Nine",
        "Eight hundred and fifty",
        "Eight hundred and fifty-One",
        "Eight hundred and fifty-Two",
        "Eight hundred and fifty-Three",
        "Eight hundred and fifty-Four",
        "Eight hundred and fifty-Five",
        "Eight hundred and fifty-Six",
        "Eight hundred and fifty-Seven",
        "Eight hundred and fifty-Eight",
        "Eight hundred and fifty-Nine",
        "Eight hundred and Sixty",
        "Eight hundred and Sixty-One",
        "Eight hundred and Sixty-Two",
        "Eight hundred and Sixty-Three",
        "Eight hundred and Sixty-Four",
        "Eight hundred and Sixty-Five",
        "Eight hundred and Sixty-Six",
        "Eight hundred and Sixty-Seven",
        "Eight hundred and Sixty-Eight",
        "Eight hundred and Sixty-Nine",
        "Eight hundred and Seventy",
        "Eight hundred and Seventy-One",
        "Eight hundred and Seventy-Two",
        "Eight hundred and Seventy-Three",
        "Eight hundred and Seventy-Four",
        "Eight hundred and Seventy-Five",
        "Eight hundred and Seventy-Six",
        "Eight hundred and Seventy-Seven",
        "Eight hundred and Seventy-Eight",
        "Eight hundred and Seventy-Nine",
        "Eight hundred and eighty",
        "Eight hundred and eighty-One",
        "Eight hundred and eighty-Two",
        "Eight hundred and eighty-Three",
        "Eight hundred and eighty-Four",
        "Eight hundred and eighty-Five",
        "Eight hundred and eighty-Six",
        "Eight hundred and eighty-Seven",
        "Eight hundred and eighty-Eight",
        "Eight hundred and eighty-Nine",
        "Eight hundred and Ninety",
        "Eight hundred and Ninety-One",
        "Eight hundred and Ninety-Two",
        "Eight hundred and Ninety-Three",
        "Eight hundred and Ninety-Four",
        "Eight hundred and Ninety-Five",
        "Eight hundred and Ninety-Six",
        "Eight hundred and Ninety-Seven",
        "Eight hundred and Ninety-Eight",
        "Eight hundred and Ninety-Nine",
        "Nine hundred",
        "Nine hundred and One",
        "Nine hundred and Two",
        "Nine hundred and Three",
        "Nine hundred and Four",
        "Nine hundred and Five",
        "Nine hundred and Six",
        "Nine hundred and Seven",
        "Nine hundred and Eight",
        "Nine hundred and Nine",
        "Nine hundred and ten",
        "Nine hundred and eleven",
        "Nine hundred and twelve",
        "Nine hundred and thirteen",
        "Nine hundred and Fourteen",
        "Nine hundred and fifteen",
        "Nine hundred and Sixteen",
        "Nine hundred and Seventeen",
        "Nine hundred and eighteen",
        "Nine hundred and Nineteen",
        "Nine hundred and twenty",
        "Nine hundred and twenty-One",
        "Nine hundred and twenty-Two",
        "Nine hundred and twenty-Three",
        "Nine hundred and twenty-Four",
        "Nine hundred and twenty-Five",
        "Nine hundred and twenty-Six",
        "Nine hundred and twenty-Seven",
        "Nine hundred and twenty-Eight",
        "Nine hundred and twenty-Nine",
        "Nine hundred and thirty",
        "Nine hundred and thirty-One",
        "Nine hundred and thirty-Two",
        "Nine hundred and thirty-Three",
        "Nine hundred and thirty-Four",
        "Nine hundred and thirty-Five",
        "Nine hundred and thirty-Six",
        "Nine hundred and thirty-Seven",
        "Nine hundred and thirty-Eight",
        "Nine hundred and thirty-Nine",
        "Nine hundred and forty",
        "Nine hundred and forty-One",
        "Nine hundred and forty-Two",
        "Nine hundred and forty-Three",
        "Nine hundred and forty-Four",
        "Nine hundred and forty-Five",
        "Nine hundred and forty-Six",
        "Nine hundred and forty-Seven",
        "Nine hundred and forty-Eight",
        "Nine hundred and forty-Nine",
        "Nine hundred and fifty",
        "Nine hundred and fifty-One",
        "Nine hundred and fifty-Two",
        "Nine hundred and fifty-Three",
        "Nine hundred and fifty-Four",
        "Nine hundred and fifty-Five",
        "Nine hundred and fifty-Six",
        "Nine hundred and fifty-Seven",
        "Nine hundred and fifty-Eight",
        "Nine hundred and fifty-Nine",
        "Nine hundred and Sixty",
        "Nine hundred and Sixty-One",
        "Nine hundred and Sixty-Two",
        "Nine hundred and Sixty-Three",
        "Nine hundred and Sixty-Four",
        "Nine hundred and Sixty-Five",
        "Nine hundred and Sixty-Six",
        "Nine hundred and Sixty-Seven",
        "Nine hundred and Sixty-Eight",
        "Nine hundred and Sixty-Nine",
        "Nine hundred and Seventy",
        "Nine hundred and Seventy-One",
        "Nine hundred and Seventy-Two",
        "Nine hundred and Seventy-Three",
        "Nine hundred and Seventy-Four",
        "Nine hundred and Seventy-Five",
        "Nine hundred and Seventy-Six",
        "Nine hundred and Seventy-Seven",
        "Nine hundred and Seventy-Eight",
        "Nine hundred and Seventy-Nine",
        "Nine hundred and eighty",
        "Nine hundred and eighty-One",
        "Nine hundred and eighty-Two",
        "Nine hundred and eighty-Three",
        "Nine hundred and eighty-Four",
        "Nine hundred and eighty-Five",
        "Nine hundred and eighty-Six",
        "Nine hundred and eighty-Seven",
        "Nine hundred and eighty-Eight",
        "Nine hundred and eighty-Nine",
        "Nine hundred and Ninety",
        "Nine hundred and Ninety-One",
        "Nine hundred and Ninety-Two",
        "Nine hundred and Ninety-Three",
        "Nine hundred and Ninety-Four",
        "Nine hundred and Ninety-Five",
        "Nine hundred and Ninety-Six",
        "Nine hundred and Ninety-Seven",
        "Nine hundred and Ninety-Eight",
        "Nine hundred and Ninety-Nine",
        "One Thousand"]

letters = 0

for i in nums:
    for j in i:
        if j.isalpha():
            letters += 1

print(letters)

# [Finished in 0.3s]
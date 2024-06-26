# Write a function that reverses characters
# in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

# Example

# For inputString = "(bar)" => "rab";
# For inputString = "foo(bar)baz" => "foorabbaz";
# For inputString = "foo(bar)baz(blim)" => "foorabbazmilb";
# For inputString = "foo(bar(baz))blim" => "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

def solution(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s

# recursive

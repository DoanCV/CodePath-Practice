# Read from the file file.txt and output all valid phone numbers to stdout.

# two regex expressions to handle (xxx) xxx-xxxx and xxx-xxx-xxxx cases
# We escape the character using \ when it is not part of the regex but is used to construct the regex
# $ is used to denote the end of a line
# ^ is used to denote the beginning of a line
# {M} is used to denote to match exactly M times of the previous occurence/regex

grep -e "\(^[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}$\)" -e "\(^([0-9]\{3\})[ ]\{1\}[0-9]\{3\}-\([0-9]\{4\}\)$\)" file.txt
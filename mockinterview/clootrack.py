# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Update all occurrences of ‘peter’ with ‘sam’ and output the number of replacements done
# method(string :str, string_to_find: str, string_to_replace: str)
# string = 'peterjppeter'
# string_to_find='peter'
# string_to_replace='sam'
# Return ('samjpsam’, 2) -> Tuple(str,int)
# Restriction: no string.replace() and string.count() and no imports






def replace_strings(orignal_string, string2, start, end):
    
    
    answer = orignal_string[:start] + string2 + orignal_string[end:]
    
    return answer


def find_and_replace(string,string_to_find, string_to_replace):
    start, end = 0, len(string_to_find)
    count = 0

    

    
    while end <= len(string):
        if string[start:end] == string_to_find:
            string = replace_strings(string, string_to_replace,start,end)
            count += 1

        start += 1
        end += 1

    return string,count


    
        

    



string = 'peterjppeter'
string_to_find='peter'
string_to_replace='p'


print(find_and_replace(string,string_to_find,string_to_replace))




                    










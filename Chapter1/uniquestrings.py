def unique_string(str):
    if len(str)>128:
        return False
    char_Set=[False for _ in range(128)]
    #print(char_Set)
    for char in str:
        val=ord(char)
        #print(val)
        if char_Set[val] :
            
            return False
        else:
            char_Set[val]=True
    return True 

print(unique_string('helo0'))

# Functions with Outputs

def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()

    # print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"

# print(format_name('KuShaL','SaINI'))


# What happenns when function has more than one return statements

# In function after return statement nothing will be executed

def format_name(f_name,l_name):
    # In this case if user passed sting empty
    if f_name =='' or l_name =='':
        return "You didn't provide valid inputs."
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()

    # print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"

print(format_name("f","g"))
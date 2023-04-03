def sort_emotions(arr, order):
    return sorted(arr, key=[':D',':)',':|',':(','T_T'].index, reverse=not order)

####################################

def sort_emotions(arr, order):
    order_dict = {
                ":D"  : 1, 
                ":)"  : 2, 
                ":|"  : 3, 
                ":("  : 4, 
                "T_T" : 5
                }
    
    return sorted(arr, key=lambda x: order_dict[x], reverse=not order)
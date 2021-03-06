####################################################################################################
# 
# PySpice - A Spice package for Python
# Copyright (C) 2014 Fabrice Salvaire
# 
####################################################################################################

####################################################################################################

def join_lines(items, prefix=''):
    return '\n'.join([prefix + str(item) for item in items if item is not None])

####################################################################################################

def join_list(items):
    return ' '.join([str(item) for item in items if item is not None])

####################################################################################################

def join_dict(d):
    return ' '.join(["{}={}".format(key, value) for key, value in d.iteritems()])

####################################################################################################
# 
# End
# 
####################################################################################################

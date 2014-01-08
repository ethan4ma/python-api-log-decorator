#!/usr/bin python
# -*- encoding=utf-8 -*-
import inspect

def api_log_decorator(function):
    '''
    A decorator function used to output api log info.
    How-to : Add @api_log_decorator just above the api function.
    '''
    def _api_log_decorator(*args, **kwargs):
        func_name = function.__name__
        inp_args = inspect.getargspec(function)
        params = inp_args[0]
        defaults = inp_args[3]
        log_str = ""

        params_dict = dict(enumerate(params))
        for p_key in params_dict.keys():
            params_dict[p_key] = {params_dict[p_key]:""}

        # deal with defaults value of the function
        if defaults:
            p_idx = len(params_dict) - len(defaults)
            for d_value in defaults:
                for k, v in params_dict[p_idx].items():
                    params_dict[p_idx][k] = d_value
                p_idx += 1

        # deal with args value of the params
        for a_idx in xrange(0, len(args)):
            for k,v in params_dict[a_idx].items():
                params_dict[a_idx][k] = args[a_idx]

        #deal with kwargs value of the params
        for k_key in kwargs.keys():
            for p_value in params_dict.values():
                if k_key in p_value:
                    p_value[k_key] = kwargs[k_key]

        # get log_info string
        log_str += "API: " + func_name
        if not params_dict:
            log_str += " Param: no params"
        for s_key, s_value in params_dict.iteritems():
            log_str += " Param[" + str(s_key+1) + "]:"
            for key, value in s_value.iteritems():
                if not value and isinstance(value, (str, unicode)):
                    log_str+= str(key) + "=" + '""'
                else:
                    log_str += str(key) + "=" + str(value)
        print log_str

        ret= function(*args, **kwargs)
        return ret
    return _api_log_decorator

# sample code
@api_log_decorator
def my_function(mode, startX1 = -1, startY1 = 1, startX2 = -1, startY2 = -1):
    print "func_test"

if __name__ == '__main__':
    #my_function(1)



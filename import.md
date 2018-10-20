## Python中模块导入的方法
    import module_name
    from module_name import function_name
    from module_name import function_name as fn
    import module_name as mn
    from module name import *
 ### import module_name
 直接导入整个模块，调用模块中函数时  
 <code>module_name.fn()</cdoe>  
 ### from module_name import function_name
 导入模块中的函数，调用函数时     
 <code>function_name()</code>  
 ### from module_name import function_name as fn
 从模块中导入函数，并给函数起个别名    
 <code>fn()</code>
 ### import module_name as mn
 导入整个模块，并赋给模块的别名是mn    
 <code>mn.function_name()</code>  
 ### from module name import *
 从模块中导入所有的函数，调用时直接写函数名    
 <code>function_name()</code>
 
   
   


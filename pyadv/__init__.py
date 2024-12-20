import platform
import subprocess
import os

def pyadv_help():
        print(r'''Pyadv Help:
        
        1. Create a variable "pyadv.project()" or "pyadv.main" without ()
        2. Use your variable to create pyadv scripts. You can do this:
            <variable name>.<command>(self)
        COMMANDS:
        x = pyadv.project()
            1. x.number(interable) - returns interable as int
            2. x.display(*args, sep=" ", end="\n") - prints args in the console with the sep and end.
            3. x.concat_strings(*args, sep=" ") - concats strings
            4. x.generate_range(start, stop, step=1) - creates a range (useful for i in range)
            5. x.custom_sum(numbers) - creates a sum (number+number)
            6. x.pyadv_Error(reason="") - generates a pyadv error
            7. x.get_input(prompt="") - generates an input.
            I cannot explain every command, sorry:(
        More help, documents and more you can find at https://pyadv.created.app/docs''')
class _pyadv:
        class Error(Exception):
                def __init__(self, message="}$}%}%"):
                        self.message = message
                        super().__init__(self.message)
null = "" if __name__ == '__main__' else False
print(f"execute pyadv project.New\n.info:\nplatform: {platform.system()}.pyadv\nExecuted: true")
os.system('''sleep 0.000001
clear''')
class main:
        def number(self, interable):
                try:
                    return int(interable)
                except Exception:
                        raise _pyadv.Error("Wrong interable name")
        def __init__(self):
            self.vars = {}
            self.commands = []
            return "pyadv.project(setupped=True)"
        # Replaces print statement, easier to use with default end as newline
        def display(self, *args, sep=' ', end='\n'):
            print(*args, sep=sep, end=end)
            
        # Easier storage view
        def storage(self):
                self.output = []
                for root, dirs, files in os.walk('.'):
                        for file in files:
                                output.append(os.path.join(root, file))
                return self.output
        
        # Better string.split() usage
        def per_space(self, variable):
            return variable.split()
    
        # Improved string concatenation
        def concat_strings(self, *args, sep=''):
            return sep.join(map(str, args))
        
        # Easier range generation
        def generate_range(self, start, stop, step=1):
            return list(range(start, stop, step))
        
        # Custom sum function
        def custom_sum(self, numbers):
            return sum(numbers)
            
        #Generate _pyadv.Error
        def pyadv_Error(reason=""):
            raise _pyadv.Error(reason)
        
        # A simplified input replacement
        def get_input(prompt=''):
            return input(prompt)
        
        # Simpler file reading
        def read_file(self, filename):
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        
        # Simpler file writing
        def write_file(self, filename, data):
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(data)
    
        # Reversed list function
        def reverse_list(self, my_list):
            return list(reversed(my_list))
        
        # Variable storage
        def assign(self, var_name, value):
            self.vars[var_name] = value
        
        # Variable retrieval
        def retrieve(self, var_name):
            return self.vars.get(var_name)
        
        # Simulating 'if' expression feature
        def conditional(self, condition, true_result, false_result):
            return true_result if condition else false_result
        
        # Range-based loop simulator
        def loop_through(self, iterable, function):
            for element in iterable:
                function(element)
        #More better error generator
        def error(text="Invalid Syntax", typef=SyntaxError):
            raise typef(text)
        #random terminal class made that doesn't even work
        class terminal:
            try:
                @staticmethod
                def __init__(self):
                    self.terminal_isDestroyed = False
                def run(self, command):
                    if self.lower() == 'cmd':
                        os.system(command)
                    elif self.lower() == 'powershell':
                        if platform.system() == 'Windows':
                            return subprocess.run(command, shell=True)
                        else:
                            raise Exception(f'Cannot run a powershell command in {platform.system()}')
                    else:
                        raise NameError(f'No command prompt program found as {self}.exe or {self}.apk')
                def destroy(self):
                    terminal_isDestroyed = True
            except Exception:
                print("I'm sorry, but that class is not working.")
        def get(pip, as_name):
                try:
                    exec(f'import {pip} as {as_name}' if as_name != null else f'import {pip}')
                except ModuleNotFoundError:
                    os.system(f'pip install {pip}')
        def oninput(
            inpt, 
            text="", 
            func=None, 
            func_obj="", 
            elsefunc="", 
            elseobj=""
        ):
                if elsefunc:
                    if inpt == text:
                        if func_obj:
                            func(func_obj)
                        else:
                            func()
                    else:
                        if elseobj:
                            elsefunc(elseobj)
                        else:
                            elsefunc()
                else:
                   if inpt == text:
                           if func_obj:
                                   func(func_obj)
                           else:
                                   func()
        class functions:
                def __init__(self):
                        print("You can also use lambdas in functions \n#!pyadv")
                def getError(self, func=None):
                        try:
                                func()
                        except Exception as e:
                                print(f"Found error: {e}")
                def execute(self, func=None):
                        func()
                def infunc(self, function=None, obj="", obj2="", obj3=""):
                        if obj2:
                            function(obj, obj2)
                        elif obj3 and obj2:
                            function(obj, obj2, obj3)
                        else:
                            function(obj)
                        if obj:
                            pass
                        else:
                            raise _pyadv.Error("Cannot leave an object null, use pyadv.Project.functions.execute(func=lambda) instead.")
        class module:
               def __init__(self):
                       self.used = []
               def delete(self, module='subprocess'):
                       self.used.append(module)
                       exec(f'del {module}')
               class xfrom:
                       def __init__(self, package):
                               self.package = package
                               self.command = False
                               while self.command == False:
                                       raise ValueError('use(self, command) is needed.')
                       def use(self, command):
                               self.command = True
                               exec(f'from {self.package} import {command}')
               def add(self, module):
                       self.used.append(module)
                       exec(f'import {module}')
        def add(self, attributte, oobject):
               attributte.append(oobject)
               if attribute not in [{}, []]:
                       raise _pyadv.Error(f'Cannot append {oobject}.')
        def equals(self, numbers):
            self.numbers = str(numbers)
            return eval(self.numbers)
            
        def loopfunc(self, func=''):
            while True:
                func()
        class execute:
                def __init__(self, code, typef):
                        if typef.lower() in ['func', 'def', 'function']:
                                code()
                        elif typef.lower() in ['code', 'python', 'py', 'pythom']:
                                exec(code)
                        elif typef.lower() in ['cmd', 'command processor']:
                                os.system(code)
                        else:
                                raise ValueError('Invalid Code type name.')
        def per_every(self, obj, do: lambda: print('', end="")):
                print("the name 'i' is the object you can change that is per every string in your object.\n#!pyadv")
                for i in obj:
                        do()
def project():
        return main
        
class Test:
    def __init__(self, root=project()):
        self.project = root
        root.display('', 'Hello! This is a test pyadv project.\n\n', end="")
        self.project.functions.execute('', func=self.example_function)
    def example_function(self):
        self.project.display('', 'This is wroten by a function!\n\nIf you write "yes" here you will "stop" the program!\n')
        self.project.loopfunc('', func=self.lip)
    def lip(self):
        self.output = self.project.get_input(prompt='Yes Or No? ')
        self.project.oninput(
            self.output.lower(), 
            text="yes", 
            func=print, 
            func_obj="[Program Finished]",
            elsefunc=print, 
            elseobj="It is still unstopped!"
        )
        
if __name__ == '__main__':
    Test()
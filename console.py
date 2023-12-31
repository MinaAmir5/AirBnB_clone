#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models.user import User
from models import storage
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb) "
    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    l_classes = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    def help_help(self):
        """ Prits help command decription """
        print("Provides description of a given command")

    def do_count(self, cls_name):
        """couts number of instnces of a class"""
        all_objs = storage.all()
        count = 0
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == cls_name:
                count = count + 1
        print(count)

    def precmd(self, arg):
        """parses commnd input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def do_show(self, arg):
        """ Shows string represetation of an intance passed """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def emptyline(self):
        """do noting when empty line"""
        pass

    def do_create(self, type_model):
        """ Creaes an instance accoding to a given class """

        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[type_model]()
            my_model.save()
            print(my_model.id)

    def do_destroy(self, arg):
        """ Deltes an insace passed """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_id = value.id
                ob_name = value.__class__.__name__
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del storage._FileStorage__objects[key]
                    del value
                    storage.save()
                    return
            print("** no instance found **")

    def do_update(self, arg):
        """ Upates an instance bsed on the class nae and id """

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                ob_id = objc.id
                ob_name = objc.__class__.__name__
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        storage.save()
                        setattr(objc, args[2], args[3])
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """ Quit comand to exit the command inerpreter """
        return True

    def do_EOF(self, line):
        """ EOF commad to exit the command iterpreter """
        return True

    def do_all(self, arg):
        """ Prints string epresention of all instnces of a given clss """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            list_instances = []
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

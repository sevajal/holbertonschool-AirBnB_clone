#! /usr/bin/python3

""" Allows you to define any variable at the package level """


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

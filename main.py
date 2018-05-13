#запускать все скрипты с директории scripts и работает с БД
import os
import importlib.util
import sys
import sqlite3
import json

#запускать все скрипты с директории scripts и работает с БД
for i in range(len(os.listdir('./scripts'))):
		importlib.import_module('scripts.{}'.format(os.listdir('./scripts')[i]).replace('.py', ''))

conn = sqlite3.connect('results.db')
curr = conn.cursor()

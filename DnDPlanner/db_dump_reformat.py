with open('db.json', 'rb') as source_file:
  with open('db.json', 'w+b') as dest_file:
    contents = source_file.read()
    dest_file.write(contents.decode('utf-16').encode('utf-8'))

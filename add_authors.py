from db import db_session, Users


authors = [
    {
         'first_name':'Василий',
         'last_name':'Петров',
         'email':'vasya@example.com'
    },
    {
         'first_name':'Маша',
         'last_name':'Иванова',
         'email':'mari@example.com'
    },
    {
         'first_name':'Петя',
         'last_name':'Смирнов',
         'email':'p@example.com'
    }
]

for a in authors:
	author = Users (a['first_name'], a['last_name'], a['email'])
	db_session.add(author)

db_session.commit()
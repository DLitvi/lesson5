import csv
import datetime
from db import Users, Post, db_session

post_list = [] 
u = Users

with open ('blog.csv', 'r', encoding = 'utf-8') as file:
	fields = ['title', 'image', 'published', 'content', 'email', 'first_name', 'last_name']
	reader = csv.DictReader(file, fields, delimiter = ';')
	for row in reader:
		row['published'] = datetime.datetime.strptime(row['published'], '%d.%m.%y %H:%M')
		author = u.query.filter(Users.email == row['email']).first()
		row['user_id'] = author.id
		print(author)
		post_list.append(row)

for post_data in post_list:
	post = Post(post_data['title'], post_data['image'], post_data['published'], post_data['content'], post_data['user_id'])
	db_session.add(post)

db_session.commit()
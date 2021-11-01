class Post:
    def __init__(self, post_id, date, author, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.date = date
        self.author = author
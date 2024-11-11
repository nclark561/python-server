from dataAccess.models import Post

def get_posts():
    return Post.query.all()

def get_post(id):
    return Post.query.get(id)

def create_post(post):
    return Post.query.create(post)

def update_post(post):
    return Post.query.update(post)

def delete_post(id):
    return Post.query.delete(id)
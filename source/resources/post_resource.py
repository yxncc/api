from flask_restful import marshal, Resource
from ..shema import PostSchema

#from ..marshalling import PostRequestParser, PostSchema
from ..extensions import db
from ..models import Post


class PostResource(Resource):


    def delete(self, post_id):
        post = Post.query.get(post_id)
        if post is None:
            return {"message": "Post not found"}, 404

        Post.query.delete()
        db.session.commit()

        return {"Post successfully deleted"}, 200

    def get (self, post_id):
        post = Post.query.get(post_id)
        if post is None:
            return {"message": "Post not found"}, 404

        return PostSchema().dump(post), 200



# """CreatePostsTable Migration."""

# from masoniteorm.migrations import Migration


# class CreatePostsTable(Migration):
#     def up(self):
#         """
#         Run the migrations.
#         """
#         with self.schema.create('posts') as table:
#             table.increments('id')
#             table.string('body')
#             table.string('title')
#             table.integer('author_id').unsigned()
#             table.foreign('author_id').references('id').on('users')
#             table.timestamps()


#     def down(self):
#         """
#         Revert the migrations.
#         """
#         self.schema.drop("posts")



from masoniteorm.migrations import Migration


class CreatePostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('posts') as table:
            table.increments('id')
            table.string('body')
            table.string('title')
            table.integer('author_id').unsigned()
            table.foreign('author_id').references('id').on('users').on_delete('CASCADE')  # Add on_delete('CASCADE') here
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("posts")

from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/blog", "BlogController@show"),
    Route.post("/blog/create", "BlogController@store"),
    Route.get("/posts", "PostController@show"),
    Route.get("/post/@id", "PostController@single"),
    Route.get("/post/@id/update", "PostController@makeUpdate"),
    Route.post("/post/@id/update", "PostController@storeUpdate"),
    Route.get('/post/@id/delete', 'PostController@delete'),
    ]
ROUTES += Auth.routes()
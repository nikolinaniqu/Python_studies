import importlib
games_mod = importlib.import_module("games")
 
print(dir(games_mod))
 
game = "GameClass"
 
game_class = getattr(games_mod,game)
game_obj = game_class()
 
print(dir(game_obj))
 
start_method = "start"
hit_method = "hit"
 
method = getattr(game_obj,start_method)
method()
method = getattr(game_obj,hit_method)
game_obj.hit(10)
game_obj.hit(20)
game_obj.hit(30)

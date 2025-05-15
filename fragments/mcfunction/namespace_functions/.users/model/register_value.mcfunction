execute as @s at @s run function namespace:.users/model/select_current_user
execute as @s at @s run data modify storage cubikframework model.cache.user.append_index set from storage cubikframework setters.index
execute as @s at @s run data modify storage cubikframework model.cache.user.append_value set from storage cubikframework setters.value
execute as @s at @s run function namespace:.users/model/write/append_data_user with storage cubikframework model.cache.user


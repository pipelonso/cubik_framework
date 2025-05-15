# Execute every time when the user enter to the world
execute as @a at @a if score @s ckflogout matches 1.. run execute if score @s ckffrsenter matches 1.. run tellraw @a "Is your first time here"
execute as @a at @a unless score @s ckflogout matches 0 run scoreboard players set @s ckflogout 0

# setting up starter values to initial scores
execute as @a at @a unless score @s lrlang matches 0 run execute unless score @s ckflang matches 1 run scoreboard players set @s lrlang 0




# At the start of the game, the computer/user score are both zero
comp_score = 0
user_score = 0

game_goal = int(input("Game Goal")) #should be a function call

# Play multiple rounds until the winner has been decided
while comp_score < game_goal and user_score < game_goal:


    # start of round loop
    # for testing purposes ask the user what the points for the user / computer were for
    comp_points = int(input("Enter the Computer Points at the end of the round"))
    user_points = int(input("Enter the User Points at the end of the round"))

    # outside round loop update score with round points, only add points to the score of the
    comp_score += comp_points
    user_score += user_points

    # show overall scores (add this to rounds loop)
    print('*** Game Update ***') #replace with call to statement generator
    print(f"User Score {user_score} | Computer Score {comp_score}")
# end of game, output final results
print()
if user_score > comp_score:
    print("You Win!") #replace this with statement generator call
else:
    print("The Computer Wins!")
'''

Raymond Nault
Chapter 5: If Statements

'''

# I'm gonna try and create an if statement on my own based on current MLB playoff teams

playoff_teams = ['Yankees', 'Astros', 'Dodgers', 'Braves', 'Rays']
eliminated_teams = ['Mets', 'Cardinals', 'Pirates', 'Blue Jays', 'Twins']

for team in playoff_teams:
    if team in playoff_teams:
        print(f"{team} has clinched a playoff spot. Good Luck!")
for team in eliminated_teams:    
    if team in eliminated_teams:
        print(f"{team} has been eliminated from playoff contention. Better luck next season!")
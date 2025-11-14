# create two sets of students in clubs
# Find all Students involved in at least one club
# Find the Students who belong to both clubs
# Find students only in the first club
# Find the students only in the second club
# Find students whoa re in exactly one club
# 2 variables

from pyscript import display

Dance = {'Jenny', 'Ashely', 'Jade', 'Aisha', 'Tar'}
Glee = {'Lia', 'Ala', 'James', 'Amanda', 'Tar'}


display(Dance & Glee, target='both') 
display(Dance - Glee, target='dance') 
display(Glee - Dance, target='glee') 
display(Dance ^ Glee, target='one')
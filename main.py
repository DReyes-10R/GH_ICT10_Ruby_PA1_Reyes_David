# create two sets of students in clubs
# Find all Students involved in at least one club
# Find the Students who belong to both clubs
# Find students only in the first club
# Find the students only in the second club
# Find students whoa re in exactly one club

from pyscript import display
# two clubs
club_A = {'James', 'Lia', 'Jade', 'Aisha', 'Tar'}
club_B = {'Lia', 'Sam', 'Jade', 'Amanda', 'Tar'}

# section
all_students = club_A | club_B
both_clubs = club_A & club_B
only_A = club_A - club_B
only_B = club_B - club_A
exactly_one = club_A ^ club_B

display(f'Club A: {sorted(club_A)}', target='output')
display(f'Club B: {sorted(club_B)}', target='output')
display(f'All students: {sorted(all_students)}', target='output')
display(f'In both clubs: {sorted(both_clubs)}', target='output')
display(f'Only in Club A: {sorted(only_A)}', target='output')
display(f'Only in Club B: {sorted(only_B)}', target='output')
display(f'In exactly one club: {sorted(exactly_one)}', target='output')
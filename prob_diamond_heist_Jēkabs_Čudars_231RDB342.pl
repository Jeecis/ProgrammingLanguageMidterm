% 231RDB342
% Defined the provided facts
person(alice, gallery1, observing_art).
person(bob, gallery1, observing_art).
person(carol, gallery2, observing_art).
person(dave, gallery2, observing_art).
person(eve, vault, inspecting_exhibit).
person(frank, vault, inspecting_exhibit).
person(grace, exhibit_hall, examining_exhibit).
person(heidi, exhibit_hall, examining_exhibit).
person(ivan, lobby, waiting).
person(judy, lobby, waiting).
person(karl, cafe, having_coffee).
person(linda, cafe, having_coffee).
person(mike, sculpture_room, admiring_art).
person(nina, sculpture_room, admiring_art).
person(oscar, ancient_art, studying_history).
person(peggy, ancient_art, studying_history).
person(quentin, modern_art, analyzing_paintings).
person(rachel, modern_art, analyzing_paintings).
person(steve, restoration_room, cleaning_artworks).
person(umar, restoration_room, cleaning_artworks).
person(valerie, library, reading_archives).
person(walter, library, reading_archives).
person(xena, storage, organizing_inventory).
person(yvonne, storage, organizing_inventory).
person(tina, security, monitoring).
person(zuzu, atrium, loitering).

% Predicate: strong_alibi(P)
% A person has a strong alibi if there is at least one other person in the same room doing the same activity.
strong_alibi(P) :-
    person(P, Room, Activity), % Finds the room and activity of the person
    person(Other, Room, Activity), % Finds another person in the same room doing the same activity
    P \= Other. % If person is not the same as the other person return true
    
% Predicate: suspicious(G)
% A person is likely guilty if no one else is in the same room doing the same activity.
suspicious(G) :-
    person(G, Room, Activity), % Finds the room and activity of the person
    % For debugging I asked copilot to print out the person that is checked
    write('Checking: '), write(G), write(' in '), write(Room), write(' doing '), write(Activity), nl, % Print out the person that is checked
    \+ (person(Other, Room, _), G \= Other), % If there is no other person in the same room return true
    % For debugging I asked copilot to print out the person that is likely guilty
    write('Likely guilty: '), write(G), nl.

% Predicate: suspect_list(L)
% The suspect list includes everyone who does not have a strong alibi.
suspect_list(L) :-
    % I asked copilot to fix my initial implementation, since it had some minor bugs
    % In short this iterates through all of the people
    % Finds a person, Checks its Alibi and checks if they are not in security room
    % If Alibi is false and person is not in security they are put in the list which later on is returned
    findall(Person, (person(Person, Room, _), \+ strong_alibi(Person), Room \= security), L).

% zuzu is guilty one
% Facts
person(alice, dining_room, playing_bridge).
person(bruno, billiard_room, playing_billiard).
person(cedrick, attic, discussing_politics).
person(dave, library, reading_books).
person(ellen, ballroom, dancing).
person(frank, conservatory, playing_piano).
person(grace, study, playing_chess).
person(harry, kitchen, dead).
person(hillary, lounge, listening_to_music).
person(ivy, dining_room, drinking_tea).
person(jack, billiard_room, painting).
person(kate, attic, playing_bridge).
person(luke, library, reading_books).
person(mary, ballroom, dancing).
person(nick, conservatory, discussing_politics).
person(nigel, garden, listening_to_music).
person(olivia, study, playing_chess).
person(paul, lounge, listening_to_music).
person(queen, dining_room, eating_cake).
person(rich, billiard_room, playing_billiard).
person(susan, attic, drinking_tea).
person(tom, library, painting).
person(ursula, ballroom, dancing).
person(victor, conservatory, discussing_politics).
person(wendy, study, playing_chess).
person(xavier, lounge, reading_books).
person(yara, dining_room, dancing).
person(zack, billiard_room, playing_billiard).

% Predicate: has_perfect_alibi(P)
% A person has a perfect alibi if there is at least one other person in the same room doing the same activity.
has_perfect_alibi(P) :-
    person(P, Room, Activity),
    person(Other, Room, Activity),
    P \= Other.

% Predicate: is_likely_guilty(G)
% A person is likely guilty if no one else is in the same room doing the same activity.
is_likely_guilty(G) :-
    person(G, Room, Activity),
    write('Checking: '), write(G), write(' in '), write(Room), write(' doing '), write(Activity), nl,
    \+ (person(Other, Room, _), G \= Other, G \= harry),
    write('Likely guilty: '), write(G), nl.

% Predicate: suspect_list(L)
% The suspect list includes everyone who is not dead.
suspect_list(L) :-
    findall(Person, (person(Person, _, _), Person \= harry), L).

% ?- has_perfect_alibi(P).
% ?- is_likely_guilty(G).
% ?- suspect_list(L).
% ?- halt.
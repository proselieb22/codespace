import random
import re

songs = [
"Bohemian Rhapsody", "Queen"
"Hey Jude", "The Beatles"
"Hotel California", "Eagles"
"Like a Rolling Stone", "Bob Dylan"
"Thriller", "Michael Jackson"
"Stairway to Heaven", "Led Zeppelin"
"Imagine", "John Lennon"
"Smells Like Teen Spirit", "Nirvana"
"Purple Haze", "Jimi Hendrix"
"Billie Jean", "Michael Jackson"
"Every Breath You Take", "The P"olice"
"Wonderwall", "Oasis"
"Sweet Child o' Mine", "Guns N' Roses"
"Someone Like You", "Adele"
"Hallelujah", "Jeff Buckley""
"Yesterday", "The Beatles"
"Livin' on a Prayer", "Bon Jovi"
"Don't Stop Believin'", "Journey"
"Shape of You", "Ed Sheeran"
"The Sound of Silence", "Simon & Garfunkel"
"My Way", "Frank Sinatra"
"I Will Always Love You", "Whitney Houston"
"Thinking Out Loud", "Ed Sheeran"
"Sweet Caroline", "Neil Diamond"
"Boogie Wonderland", "Earth, Wind & Fire"
"I Want to Hold Your Hand", "The Beatles"
"I Will Survive", "Gloria Gaynor"
"Waterloo", "ABBA"
"Tears in Heaven", "Eric Clapton"
"Wannabe", "Spice Girls"
"A Thousand Years", "Christina Perri"
"Clocks", "Coldplay"
"Rolling in the Deep", "Adele"
"Born to Run", "Bruce Springsteen"
"Under Pressure", "Queen & David Bowie"
"The Winner Takes It All", "ABBA"
"Dancing Queen", "ABBA"
"Let It Be", "The Beatles"
"Boogie Woogie Bugle Boy", "The Andrews Sisters"
"Good Vibrations", "The Beach Boys"
"All of Me", "John Legend"
"Firework", "Katy Perry"
"I Say a Little Prayer", "Aretha Franklin"
"Nothing Else Matters", "Metallica"
"Angels", "Robbie Williams"
"Radioactive", "Imagine Dragons"
"Ain't No Mountain High Enough", "Marvin Gaye & Tammi Terrell"
"Love Me Tender", "Elvis Presley"
"Purple Rain", "Prince"
"Respect", "Aretha Franklin"
"I Want You Back", "The Jackson 5"
"With or Without You", "U2"
"Blackbird", "The Beatles"
"I Gotta Feeling", "The Black Eyed Peas"
"Let's Get It On", "Marvin Gaye"
"September", "Earth, Wind & Fire"
"Summertime", "Ella Fitzgerald & Louis Armstrong
"Your Song", "Elton John"
"Three Little Birds", "Bob Marley & The Wailers"
"All You Need Is Love", "The Beatles"
"I Heard It Through the Grapevine", "Marvin Gaye"
"What a Wonderful World", "Louis Armstrong"
"Don't You Want Me",  "The Human League"
"Sweet Dreams (Are Made of This)", "Eurythmics"
"Roxanne", "The Police"
"No Woman, No Cry", "Bob Marley & The Wailers"
"Faith", "George Michael"
"Killing Me Softly With His Song", "Roberta Flack"
"Help!", "The Beatles"
"Crazy", "Gnarls Barkley"
"Vogue", "Madonna"
"Dreams", "Fleetwood Mac"
"Space Oddity", "David Bowie"
"All Night Long (All Night)", "Lionel Richie"
"Unforgettable", "Nat King Cole"
"Brown Eyed Girl", "Van Morrison"
"Highway to Hell", "AC/DC"
"I'm Yours", "Jason Mraz"
"Heaven", "Bryan Adams"
"Let's Stay Together", "Al Green"
"Kiss From a Rose", "Seal"
"A Change Is Gonna Come", "Sam Cooke"
"It Must Have Been Love", "Roxette"
"You're Beautiful", "James Blunt
]
def main():
    input('\nHello, press enter to play hangman!')
    print('\nEnter -e or --exit to end game')
    print('Enter -r or --retry to restart game with another movie.\n\n')


    # select a random movie
    movie, year = select_movie(films)

    # print movie name and year - DEMO
    # print(f'(Demo purpose - Movie name : {movie})\n')

    # frame question with blanks
    ques = question(movie)

    # create list of moviename
    movie_list = [letter for letter in movie]

    # run game and get result
    res = game(ques, movie_list, year)

    if res == 'exit':
        print('Game Ended.')
        return
    if res == True or res == False:
        print(get_result(res))


def select_movie(films):
    movie = random.choices(films)

    if search := re.search(r'^([A-Za-z0-9_.-:,\' ]*) \((\d{4})\)$', movie[0]):
        return search.groups()


def question(movie_name):
    q = []
    for letter in movie_name:
        if letter.isalpha() or letter.isnumeric():
            q.append('_')
        else:
            q.append(letter)

    return q


def game(question, movie, year):

    # create moviename in str
    moviename = ''.join(map(str, movie)).strip().lower()

    # copy moviename list
    moviecp = movie.copy()

    # create a list of all elements of movie in lowercase
    lower_movie = [x.lower() for x in movie]

    # initiate counter
    count = 1
    hint = False

    while count < 11 and '_' in question:
        print(*question, '\n')

        if count > 5 and hint == False:
            print('To get hint, enter \'--hint\'\n')

        answer = input(f'Guess a character or the movie name ({11-count} chances left): ').lower().strip()

        if answer == '--hint' and count > 5 and hint == False:
            print(f'The movie was released in {year}\n')
            hint = True

        elif answer == '--exit' or answer == '-e' or answer == '--quit':
            return 'exit'

        elif answer == '-r' or answer == '--retry':
            print('\n')
            return main()

        elif answer in lower_movie:
            while answer in lower_movie:
                index = lower_movie.index(answer)
                question[index] =  moviecp[index]
                lower_movie[index] = 'NULL'

        elif answer == moviename:
            question=moviecp.copy()
            break

        else:
            # if wrong guess increase counter
            count+=1

    if count < 11:
        print(*question,'\n')
        return True
    return False


def get_result(result):
    if result:
        return 'Correct!'
    else:
        return 'Incorrect, try again!'


if __name__ == "__main__":
    main()

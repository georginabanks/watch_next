# import spacy
import spacy
nlp = spacy.load('en_core_web_md')

# read movies text file
f = open('movies.txt', 'r')
movies = f.readlines()
f.close()

# planet hulk description
planet_hulk = nlp("""Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, 
the illuminati trick Hulk into a shuttle and launch him 
into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is 
sold into slavery and trained as a gladiator.""")

# find movie with the highest similarity
highest = 0
next_movie = 0

for i in movies:
    movie = nlp(i)
    similarity = planet_hulk.similarity(movie)
    if similarity > highest:
        highest = similarity
        next_movie += 1

# watch movie with the highest similarity
watch_next = movies[next_movie].replace('\n', '')

print(f'You should watch: \n"{watch_next}"')


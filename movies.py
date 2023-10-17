from flask import Flask, jsonify, request
app = Flask(__name__)
movies = (
    {
        "name":"Iron Man",
        "casts": ["Tony Stark", "Happy"],
        "genre": ["Action", "Sci Fi"]
    }
)
@app.route('/movies', methods=['Get'])
def getMovies():
    return jsonify(movies)
@app.route('/movies',methods=['POST'])
def add_movie():
    movies = request.get_json()
    movies.append(movie)
    return{}
if __name__=='__main__':
    app.run()
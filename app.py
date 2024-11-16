from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load the dataset
music_df = pd.read_csv('music.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '').lower()
    results = []
    
    if query:
        for index, row in music_df.iterrows():
            if query in str(row['lyrics']).lower():
                results.append({
                    'artist': row['artist_name'],
                    'music_name': row['track_name'],
                    'lyrics': row['lyrics'],
                    'id': index
                })
    
    return render_template('results.html', results=results, query=query)

@app.route('/lyrics/<int:music_id>')
def show_lyrics(music_id):
    music_data = music_df.iloc[music_id]
    return render_template(
        'lyrics.html',
        artist=music_data['artist_name'],
        music_name=music_data['track_name'],
        lyrics=music_data['lyrics']
    )

if __name__ == '__main__':
    app.run(debug=True)

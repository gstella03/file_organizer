from flask import Flask, render_template, request, redirect, url_for, flash
import logging
from organizer import organize_files

# Creazione di un'app Flask
app = Flask(__name__)

# Impostazione della chiave segreta necessaria per i messaggi flash
app.secret_key = 'your_secret_key'  

# Configurazione del logging per registrare messaggi in un file
logging.basicConfig(
    filename='logs/file_organizer.log',    # Nome del file di log
    level=logging.DEBUG,                   # Livello di log (DEBUG registra tutti i livelli di log)
    datefmt='%d/%m/%y %H:%M:%S',           # Formato della data nei log
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del messaggio di log
)

# Route per la homepage dell'app
@app.route('/')
def index():
    return render_template('index.html')  # Renderizza il template HTML index.html

# Route per gestire la richiesta di organizzazione dei file
@app.route('/organize', methods=['POST'])
def organize():
    # Ottiene i dati inviati dal form (directory e metodo di organizzazione)
    directory = request.form.get('directory')
    method = request.form.get('method')
    
    try:
        # Prova a organizzare i file nella directory specificata utilizzando il metodo scelto
        organize_files(directory, method)
        # Se tutto va bene, mostra un messaggio di successo all'utente
        flash('Organizzazione completata con successo!', 'success')
    except ValueError as e:
        # Se c'è un errore, mostra un messaggio di errore all'utente e registra l'errore nei log
        flash(str(e), 'error')
        logging.error(f"Error: {e}")
    
    # Reindirizza l'utente alla homepage dopo aver processato la richiesta
    return redirect(url_for('index'))

# Avvia l'app Flask in modalità debug
if __name__ == '__main__':
    app.run(debug=True)


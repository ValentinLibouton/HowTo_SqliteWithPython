import sqlite3

DB_NAME = 'ma_base_de_donnees.db'
def create_db(DB_NAME):
    # Connexion à la base de données (cela créera un fichier de base de données s'il n'existe pas)
    conn = sqlite3.connect(DB_NAME)

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = conn.cursor()

    # Définition de la requête SQL pour créer une table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS MaTable (
        id INTEGER PRIMARY KEY,
        nom TEXT,
        age INTEGER
    );
    '''

    # Exécution de la requête SQL
    cursor.execute(create_table_query)

    # Valider les changements et fermer la connexion
    conn.commit()
    conn.close()

def insert_data_in_db(DB_NAME, nom, age):
    # Connexion à la base de données
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Requête SQL d'insertion
    insert_query = '''
        INSERT INTO MaTable (nom, age)
        VALUES (?, ?);
        '''

    # Exécution de la requête SQL avec les valeurs à insérer
    cursor.execute(insert_query, (nom, age))

    # Valider les changements et fermer la connexion
    conn.commit()
    conn.close()

    # Exemple d'utilisation de la fonction d'insertion

def read_data_in_db(DB_NAME):
    # Connexion à la base de données
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Requête SQL pour récupérer toutes les données
    select_query = '''
    SELECT * FROM MaTable;
    '''

    # Exécution de la requête SQL
    cursor.execute(select_query)

    # Récupération de toutes les lignes
    rows = cursor.fetchall()

    # Fermer la connexion
    conn.close()

    return rows


if __name__=='__main__':
    create_db(DB_NAME)
    insert_data_in_db(DB_NAME, "John Doe", 30)
    insert_data_in_db(DB_NAME, "Jane Doe", 25)
    datas_in_db = read_data_in_db(DB_NAME)
    for i, row in enumerate(datas_in_db):
        print(f"La ligne {i} contient: {row}")
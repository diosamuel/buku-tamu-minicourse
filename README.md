# Projek Buku Tamu

## Dependencies

```pip install -r requirements.txt```

## Usage

Untuk kebutuhan penyimpanan data, buat database bernama bukutamu pada mysql

```sql
CREATE DATABASE bukutamu
```

Buat table comments pada database bukutamu tersebut
```sql
CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `comment` text NOT NULL
)
```
Pada file utama web, yaitu guestbook.py (baris ke 5), ganti isi username dan password dengan username dan password mysql Anda
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost:3306/bukutamu'
```
Jalankan web dengan perintah

```bash
python guestbook.py
```


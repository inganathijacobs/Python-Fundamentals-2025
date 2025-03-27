## Schema

```sql
CREATE TABLE artists (
    artist_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    birth_year INT NOT NULL
);

CREATE TABLE artworks (
    artwork_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    artist_id INT NOT NULL,
    genre VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);
```

## Sample Data

```sql
INSERT INTO artists (artist_id, name, country, birth_year) VALUES
(1, 'Vincent van Gogh', 'Netherlands', 1853),
(2, 'Pablo Picasso', 'Spain', 1881),
(3, 'Leonardo da Vinci', 'Italy', 1452),
(4, 'Claude Monet', 'France', 1840),
(5, 'Salvador Dalí', 'Spain', 1904),
(6, 'Frida Kahlo', 'Mexico', 1907);

INSERT INTO artworks (artwork_id, title, artist_id, genre, price) VALUES
(1, 'Starry Night', 1, 'Post-Impressionism', 1000000.00),
(2, 'Sunflowers', 1, 'Post-Impressionism', 800000.00),
(3, 'Guernica', 2, 'Cubism', 2000000.00),
(4, 'Mona Lisa', 3, 'Renaissance', 3000000.00),
(5, 'The Persistence of Memory', 5, 'Surrealism', 1500000.00),
(6, 'Water Lilies', 4, 'Impressionism', 500000.00),
(7, 'Irises', 1, 'Post-Impressionism', 900000.00),
(8, 'Les Demoiselles d''Avignon', 2, 'Cubism', 1800000.00),
(9, 'The Last Supper', 3, 'Renaissance', 2800000.00),
(10, 'The Weeping Woman', 2, 'Cubism', 1700000.00);
```

1.  Write a query to list all artworks where the title contains 'Night', sorted by title in ascending order.

```sql
SELECT \* FROM artworks
WHERE title LIKE '%Night%'
```

2.  Write a query to display each artist with the total number of artworks they have created, including artists with no artworks, sorted in descending order by the artwork count.

```sql
SELECT artists.name, sum(artworks.artist_id) as Total_Artworks  FROM artists
left join artworks
on artists.artist_id = artworks.artist_id
group by artists.name
order by Total_Artworks
```

3.  Write a query to display the average price of artworks for each genre, only including genres where the average price is above 800000, sorted by genre name.

```sql
select genre, avg(price) as average_price from artworks
group by genre
having average_price>800000
order by genre
```

2.  Write a query to list all artists who do not have any artworks in the artworks table.

```sql
select artists.name from artists full join artworks
on artists.artist_id= artworks.artist_id
where artworks.artwork_id is null

```

-- Задание 2 
-- Название и продолжительность самого длительного трека 
SELECT track_name, duration
FROM track_list
ORDER BY duration DESC  
LIMIT 1;

-- Название треков, продолжительность которых не менее 3,5 минут
SELECT track_name, duration 
FROM track_list
WHERE duration > 210

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT compilation_name 
FROM compilations
WHERE releaseyear BETWEEN 2018 AND 2020

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT MAX(artist_name)
FROM artists



CREATE TABLE Artists (
	ArtistID INT PRIMARY KEY,
	artist_name VARCHAR(255)
);

CREATE TABLE Genres (
	GenreID INT PRIMARY KEY,
	genre_name VARCHAR(255)
);

CREATE TABLE artists_genres (
	ID INT PRIMARY KEY,
	ArtistID INT,
	GenreID INT,
	FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID),
	FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
);

CREATE TABLE Albums (
	AlbumID INT PRIMARY KEY,
	album_name VARCHAR(255),
	release_year INT
);

CREATE TABLE Artist_Albums (
	ID INT PRIMARY KEY,
	ArtistID INT,
	AlbumID INT,
	FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID),
	FOREIGN KEY (AlbumID) REFERENCES Albums(AlbumID)
);

CREATE TABLE Track_list (
    TrackID INT PRIMARY KEY,
    track_name VARCHAR(255),
    Duration INT,
    AlbumID INT,
    FOREIGN KEY (AlbumID) REFERENCES Albums(AlbumID)
);

CREATE TABLE Compilations (
    CompilationID INT PRIMARY KEY,
    Compilation_name VARCHAR(255),
    ReleaseYear INT
);

CREATE TABLE Track_Compilations (
    ID INT PRIMARY KEY,
    TrackID INT,
    CompilationID INT,
    FOREIGN KEY (TrackID) REFERENCES Track_list(TrackID),
    FOREIGN KEY (CompilationID) REFERENCES Compilations(CompilationID)
);
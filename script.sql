CREATE DATABASE bibliotheque;

insert into categories (libelle_categorie) values('Roman'), ('Geographie'), ('Histoire'), ('Philosophie'), ('Developpement personnel'), ('Theatre'), ('Theologie'), ('Contes'), ('Auto-biographie'), ('Bandes déssinée'), ('Comics')

insert into livres(isbn, titre, date_publication, auteur, editeur, categorie_id) 
			values ('978-2-213-70787-7' ,'Devenir', '30-11-2018', 'Michelle OBAMA','Librairie Artheme Fayard', 9),
                    ('979-10-92928-07-5' ,'Power - Les 48 lois du pouvoir', '31-12-1998', 'Robert GREENE','Les editions Leduc.s', 5),
('9780230013858' ,'Un long chemin vers la liberte', '30-11-1994', 'Nelson MANDELA','Livre de poche', 9),
                    ('9780977476077' ,'Mein Kampf', '18-07-1925', 'Adolf HITLER','Reluire à la française', 3),
                    ('2-221-08625-2' ,'Le pharaon noir', '31-12-1997', 'Christian JACQ','Robert LAFFONT', 1),
('978-2-910188-13-9' ,'L''Alchimiste', '31-12-1988', 'Paulo Coelho','Anne Carriere', 1),
                    ('978-2-212-54434-3' ,'L''art de negocier avec la methode Harvard', '31-12-2009', 'Maurice A. Bercoff','Eyrolles', 5),
                    ('9782737363955' ,'Atlas mondial', '31-12-2001', 'Patrick Merienne','Patrick Merienne', 2),
                    ('9780863560231' ,'Les Croisades vues par les Arabes', '31-12-1983', 'Amin Maalouf','Livre de poche', 3),
                    ('978-2-07-032913-7' ,'L''existentialisme est un humanisme', '31-12-1946', 'Jean-Paul Sartre','Editions Nagel', 4),
                    ('9782213718620' ,'Des profondeurs de nos coeurs', '15-01-2020', 'Benoît XVI et Robert Sarah','Fayard', 7),
                    ('9782213686103' ,'Dieu ou rien: Entretien sur la foi', '25-02-2015', 'Nicolas Diat et Robert Sarah','Fayard', 7);


  
CREATE TABLE adoption (
    pet_id INT,
    pet_name VARCHAR(50),
    pet_species VARCHAR(50),
    pet_habitat VARCHAR(50),
    adopter_name VARCHAR(50),
    adopter_age INT,
    adopter_residence VARCHAR(50),
    magical_power VARCHAR(255),
    godparent_name VARCHAR(50),
    wand_type VARCHAR(50),
    godparent_speciality VARCHAR(50),
    godparent_residence VARCHAR(50),
    CONSTRAINT pk_pet_id PRIMARY KEY (pet_id)
);

INSERT INTO adoption (
    pet_id, pet_name, pet_species, pet_habitat, adopter_name, adopter_age, adopter_residence, magical_power, godparent_name, wand_type, godparent_speciality, godparent_residence
) VALUES
(1, 'Fluffy', 'Dragon', 'Cave', 'John Doe', 35, 'Enchanted Forest', 'Fire Breathing', 'Fairy Godmother', 'Oak Wand', 'Transformation', 'Fairyland'),
(2, 'Whiskers', 'Cat', 'House', 'Jane Smith', 28, 'Magic City', 'Invisibility', 'Wizard Elder', 'Crystal Staff', 'Healing', 'Elder Tower'),
(3, 'Spark', 'Phoenix', 'Fire Nest', 'Harry Potter', 40, 'Hogwarts', 'Rebirth', 'Fairy Godmother', 'Oak Wand', 'Transformation', 'Fairyland'),
(4, 'Shadow', 'Wolf', 'Forest', 'Alice Wonderland', 30, 'Wonderland', 'Teleportation', 'Sorcerer Supreme', 'Mystical Orb', 'Elemental Control', 'Mystic Realm');
(5, 'Shadow', 'Wolf', 'Forest', 'Alice Wonderland', 30, 'Wonderland', 'Teleportation', 'Wizzy Wizard', 'Mystical Globe', 'Force Push', 'Golden Glade');
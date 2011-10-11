--
-- Query to translate term in SQL query
--
CREATE OR REPLACE FUNCTION get_trad(langue varchar, typ varchar, nom varchar, texte varchar) RETURNS varchar AS $$
	DECLARE
	  resultat text;
	  resultat1 text;

        BEGIN
		IF texte is not null then
			select into resultat value::text from ir_translation where lang=langue and type=typ and name=nom and src=texte;
		ELSE
			select into resultat value::text from ir_translation where lang=langue and type=typ and name=nom;
		END IF;
		IF NOT FOUND THEN
			RETURN texte;
		ELSE
			RETURN resultat;
		END IF;
        END;
$$ LANGUAGE plpgsql;

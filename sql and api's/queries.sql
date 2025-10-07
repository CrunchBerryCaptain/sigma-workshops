SELECT (title) 
FROM media as m
JOIN media_type as mt
ON m.media_type_id = mt.media_type_id
WHERE mt.media_type_name='shows'
;
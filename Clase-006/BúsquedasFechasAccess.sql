SELECT * FROM vuelos WHERE
DateDiff('y',fechadesde,now())>=0
and DateDiff('y',fechahasta,nom())<=0

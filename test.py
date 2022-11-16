import pyarrow.parquet as pq

table2 = pq.read_table('data/pokemons.parquet')
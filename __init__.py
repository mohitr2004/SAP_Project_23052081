2026-04-16T14:01:09 | INFO     | csv_pipeline | ============================================================
2026-04-16T14:01:09 | INFO     | csv_pipeline | Pipeline starting
2026-04-16T14:01:09 | INFO     | csv_pipeline |   input_dir     : data
2026-04-16T14:01:09 | INFO     | csv_pipeline |   output_path   : output\merged_output.csv
2026-04-16T14:01:09 | INFO     | csv_pipeline |   fill_strategy : median
2026-04-16T14:01:09 | INFO     | csv_pipeline |   drop_threshold: 50%
2026-04-16T14:01:09 | INFO     | csv_pipeline | ============================================================
2026-04-16T14:01:09 | INFO     | csv_pipeline | Loaded orders.csv                                rows=6        cols=6     (0.013s)
2026-04-16T14:01:09 | INFO     | csv_pipeline | Loaded products.csv                              rows=5        cols=5     (0.003s)
2026-04-16T14:01:09 | INFO     | csv_pipeline | Loaded users.csv                                 rows=6        cols=5     (0.002s)
2026-04-16T14:01:09 | INFO     | csv_pipeline | [orders] Imputed 2 nulls via strategy='median'
2026-04-16T14:01:09 | INFO     | csv_pipeline | [orders] Cleaning complete: (6, 6) -> (6, 6)
2026-04-16T14:01:09 | INFO     | csv_pipeline | [products] Imputed 2 nulls via strategy='median'
2026-04-16T14:01:09 | INFO     | csv_pipeline | [products] Cleaning complete: (5, 5) -> (5, 5)
2026-04-16T14:01:09 | INFO     | csv_pipeline | [users] Imputed 2 nulls via strategy='median'
2026-04-16T14:01:09 | INFO     | csv_pipeline | [users] Removed 1 duplicate row(s)
2026-04-16T14:01:09 | INFO     | csv_pipeline | [users] Cleaning complete: (6, 5) -> (5, 5)
2026-04-16T14:01:09 | INFO     | csv_pipeline | No join keys specified — concatenating 3 frame(s)
2026-04-16T14:01:09 | INFO     | csv_pipeline | Merged result: rows=16  cols=13
2026-04-16T14:01:09 | INFO     | csv_pipeline | Output written -> output\merged_output.csv
2026-04-16T14:01:09 | INFO     | csv_pipeline | Pipeline finished in 0.08s

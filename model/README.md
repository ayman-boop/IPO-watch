# model/

The model is developed here, separately from the data scripts in `scripts/`.

## Input
`data/small/dataset.csv`, one row per IPO, built by `scripts/s5_build_dataset.py`:

| column | meaning |
|---|---|
| `first_trade_date` | used to split train/test by time (not a feature) |
| `price_vs_range` | (final price − range midpoint) / midpoint |
| `range_width` | (high − low) / midpoint |
| `log_proceeds` | log(final price × shares offered) |
| `is_nasdaq` | 1 if listed on Nasdaq |
| `vix` | VIX close on pricing date |
| `nasdaq_30d` | Nasdaq return over the 30 days before pricing |
| **`day1_return`** | **target**: day-1 close / final price − 1 |

## Plan
`src/train_small.py`: time split (oldest 75% train / newest 25% test), then compare
baseline (median) → linear on `price_vs_range` → linear on all → depth-3 tree.
Metrics: MAE and direction accuracy. See `docs/START_SMALL.txt` step 6.

# model/

Your pricing / first-week trading model is developed here, separately from the data pipeline in `src/ipo_watch`.

## Interface with the pipeline

**Input** (produced by `ipo_watch.features`):
- Table `feature_snapshots(deal_id, as_of, feature_name, value, topic, sources)`. Point-in-time: every value was known at `as_of`.
- Table `outcomes(deal_id, final_price, open_d1, close_d1..close_d5, volume_d1..d5)`. These are the targets.
- Or the parquet files exported by `ipo_watch.features.export` into `data/processed/`.

**Output** (read back by the pipeline / dashboard):
- Table `predictions(deal_id, as_of, target, p10, p50, p90, model_version, shap)`.

Targets: `T1` final price vs range · `T2` day-1 open pop · `T3` day-1 close · `T4` day-5 close · `T5` week-1 volatility (see `docs/PLAN.txt` §3).

## Layout
- `src/` holds model code (training, prediction, evaluation).
- `notebooks/` is for exploration.

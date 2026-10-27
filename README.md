# IPO-watch

Predict an IPO's day-1 return from SEC filings and market context, starting with a small,
end-to-end pipeline. Step-by-step plan: [`docs/START_SMALL.txt`](docs/START_SMALL.txt).

## Setup

```bash
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.example .env        # put your name + email in SEC_USER_AGENT
```

## Layout

```
IPO-watch/
├── scripts/            # pipeline steps, run in order; each reads the previous CSV
│   ├── edgar_utils.py  #   shared: EDGAR GET with User-Agent, rate limit, local cache
│   ├── s1_list_ipos.py     → data/small/01_ipos.csv
│   ├── s2_extract_terms.py → data/small/02_terms.csv
│   ├── s3_outcomes.py      → data/small/03_outcomes.csv
│   ├── s4_market.py        → data/small/04_market.csv
│   └── s5_build_dataset.py → data/small/dataset.csv
├── model/src/          # train_small.py: baseline vs linear vs small tree
├── data/
│   ├── small/          # the step CSVs (git-ignored)
│   └── cache/          # downloaded filings (git-ignored)
├── tests/              # created with the first script
└── docs/               # START_SMALL.txt (current), PLAN.txt + ARCHITECTURE.txt (long-term)
```

Run a step: `.venv/bin/python scripts/s1_list_ipos.py`

The full-scale layout (database, collectors, signals) is in commit `53e802a` and
`docs/ARCHITECTURE.txt`, for when the small version works.
